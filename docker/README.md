### docker

Run dockerfile to:
- download python repo
- install requirements
- run unittests

Run:
`docker-compose -f docker-compose.yaml up --build`

Expected output:
```
[+] Building 1.4s (10/10) FINISHED                         docker:desktop-linux
 => [main internal] load build definition from dockerfile                  0.0s
 => => transferring dockerfile: 274B                                       0.0s
 => [main internal] load metadata for docker.io/library/python:3           1.3s
 => [main auth] library/python:pull token for registry-1.docker.io         0.0s
 => [main internal] load .dockerignore                                     0.0s
 => => transferring context: 2B                                            0.0s
 => [main 1/4] FROM docker.io/library/python:3@sha256:e3d5b6f95ce66923b5e  0.0s
 => CACHED [main 2/4] RUN git clone https://github.com/2dot71mily/baby_re  0.0s
 => CACHED [main 3/4] RUN cd baby_repo && pip3 install -r requirements.tx  0.0s
 => CACHED [main 4/4] WORKDIR baby_repo                                    0.0s
 => [main] exporting to image                                              0.0s
 => => exporting layers                                                    0.0s
 => => writing image sha256:ecce6ac4c21273b06020515ea0cac0b02f0e2f0720eb6  0.0s
 => => naming to docker.io/library/docker-main                             0.0s
 => [main] resolving provenance for metadata file                          0.0s
[+] Running 2/1
 ✔ Network docker_default   Created                                        0.0s 
 ✔ Container docker-main-1  Created                                        0.0s 
Attaching to main-1
main-1  | ..................
main-1  | ----------------------------------------------------------------------
main-1  | Ran 18 tests in 0.053s
main-1  | 
main-1  | OK
main-1 exited with code 0
```