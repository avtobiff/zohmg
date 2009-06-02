#Licensed to the Apache Software Foundation (ASF) under one
#or more contributor license agreements.  See the NOTICE file
#distributed with this work for additional information
#regarding copyright ownership.  The ASF licenses this file
#to you under the Apache License, Version 2.0 (the
#"License"); you may not use this file except in compliance
#with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an
#"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#KIND, either express or implied.  See the License for the
#specific language governing permissions and limitations
#under the License.

import time

# TODO: rename => 'static'
class client(object):
    """
    Application that serves static files from the 'static' directory in the
    project directory.
    """
    def __call__(self,environ,start_response):
        from paste.urlparser import make_static
        project_dir = environ["zohmg_project_dir"]
        file = environ["PATH_INFO"]
        # TODO: file == '' => 'index.html'
        client = make_static({}, project_dir+"/static")
        print "[%s] Client, serving static file %s%s." % (time.asctime(), project_dir, file)
        return client(environ, start_response)
