import os
import sys

import boto3

from src.constants import (
	AWS_ACCESS_KEY_ID_ENV_KEY,
	AWS_SECRET_ACCESS_KEY_ENV_KEY,
	REGION_NAME,
)
from src.exception import MyException


class S3Client:
	"""Small helper for creating a boto3 S3 client.

	Uses credentials from environment variables by default.
	"""

	def __init__(self, region_name: str = REGION_NAME) -> None:
		try:
			access_key = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
			secret_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

			if access_key and secret_key:
				self._client = boto3.client(
					"s3",
					aws_access_key_id=access_key,
					aws_secret_access_key=secret_key,
					region_name=region_name,
				)
			else:
				self._client = boto3.client("s3", region_name=region_name)
		except Exception as e:
			raise MyException(e, sys)

	@property
	def client(self):
		return self._client
