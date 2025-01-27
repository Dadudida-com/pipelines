# Copyright 2018 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages


setup(
  name='trainer',
  version='1.0.0',
  packages=find_packages(),
  description='DNN Trainer',
  author='Google',
  keywords=[
  ],
  license="Apache Software License",
  long_description="""
  """,
  install_requires=[
    'tensorflow==2.11.1',
  ],
  package_data={
  },
  data_files=[],
)
