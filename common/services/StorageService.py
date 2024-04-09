import os
import pathlib
from pathlib import Path
from datetime import datetime
from shutil import copyfile

import boto3

from ccresponse import settings
from common.helpers.CommonHelper import random_string
from common.helpers.FilesHelper import secure_filename


class StorageService(object):
    def __init__(self):
        # S3 Object Storage Initialize
        self.__session = boto3.session.Session()
        self.__s3 = self.__session.client(
            's3', settings.AWS_S3_REGION_NAME,
            endpoint_url='https://ams3.digitaloceanspaces.com',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        # Local Storage Initialize
        self.__local_storage_path = None

    def initialize_local(self, storage_path):
        self.__local_storage_path = storage_path

    def __is_local_storage_initialized(self):
        if self.__local_storage_path is None:
            raise Exception('Local Storage is not initialized')

    def __is_s3_storage_initialized(self):
        if self.__s3 is None:
            raise Exception('S3 Object Storage is not initialized')

    def get_local_storage_path(self):
        self.__is_local_storage_initialized()
        return self.__local_storage_path

    def make_local_full_path(self, relative_path):
        self.__is_local_storage_initialized()
        return f'{self.__local_storage_path}/{relative_path}'

    def __create_local_folder(self, folder):
        dir_path = self.make_local_full_path(folder)
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        return dir_path

    @staticmethod
    def __process_filename(filename, store_original_filename=True, store_secure_filename=True, timestamp_append=True):
        if not store_original_filename:
            _, file_extension = os.path.splitext(filename)
            filename = f'{random_string(32)}{file_extension}'

        if timestamp_append:
            filename = f'{datetime.utcnow().strftime("%Y%m%d-%H%M%S-%f")}-{filename}'

        if store_secure_filename:
            filename = secure_filename(filename)
        return filename

    def copy_local(self, rel_from_file, to_folder, to_filename):
        self.__is_local_storage_initialized()

        dir_path = self.__create_local_folder(to_folder)

        rel_file_path = f'{to_folder}/{to_filename}'
        abs_file_path = f'{dir_path}/{to_filename}'

        copyfile(self.make_local_full_path(rel_from_file), abs_file_path)
        return rel_file_path

    def put_into_s3_from_stream(self, file_stream, folder, file_name, store_original_filename=True,
                                store_secure_filename=True, timestamp_append=True, mimetype=None):
        '''
        Method for uploading a file into s3 from bytes stream.

        Args:
            file_stream ([FileStorage, io.BytesIO, etc]): stream of bytes of file. This object should implement the read() method which return the bytes (b"")
            folder ([str]): folder in bucket
            file_name ([str]): original file name. If you don't know the file name, but know only file exctension (ex. pdf), use the file_name='_.pdf' and store_original_filename=False
            store_original_filename (bool, optional): The flag for saving of original file name. Defaults to True.
            store_secure_filename (bool, optional): The flag for store file name with secure. Defaults to True.
            timestamp_append (bool, optional): The flag for adding the time stamp to file name. Defaults to True.
            mimetype (str, optional): The flag for adding the mimetype for file
        Returns:
            [str]: relative path of file
        '''
        upload_file_name = self.__process_filename(file_name, store_original_filename, store_secure_filename,
                                                   timestamp_append)
        rel_file_path = f'{folder}/{upload_file_name}'

        if mimetype is not None:
            self.__s3.upload_fileobj(file_stream, settings.AWS_STORAGE_BUCKET_NAME, rel_file_path, ExtraArgs={'ContentType': mimetype})
        else:
            self.__s3.upload_fileobj(file_stream, settings.AWS_STORAGE_BUCKET_NAME, rel_file_path)
        return rel_file_path

    def delete_s3(self, rel_file_path):
        self.__is_s3_storage_initialized()
        self.__s3.delete_objects(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Delete={'Objects': [{'Key': rel_file_path}]})

    def get_from_s3_to_bytes(self, rel_file_path):
        s3_obj = self.__s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=rel_file_path)
        data = s3_obj['Body'].read()
        return data

    def get_from_s3_to_local(self, rel_file_path):
        self.__is_local_storage_initialized()
        self.__is_s3_storage_initialized()
        # create local directory
        pathlib.Path(rel_file_path).parent.mkdir(parents=True, exist_ok=True)
        abs_file_path = self.make_local_full_path(rel_file_path)
        self.__s3.download_file(settings.AWS_STORAGE_BUCKET_NAME, rel_file_path, abs_file_path)

    def get_s3_presigned_url(self, rel_file_path, expiration=3600):
        self.__is_s3_storage_initialized()

        return self.__s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': rel_file_path,
            },
            HttpMethod="GET",
            ExpiresIn=expiration
        )


storageService = StorageService()
