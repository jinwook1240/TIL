# How to build Chromium QUIC
# 크로미엄 QUIC을 빌드하는 방법  
## 크로미엄 받기, 환경 설정
[이 링크](https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions.md#install)에서 크로미엄 소스를 내려받는 방법을 볼 수 있다.  
`Install depot_tools`, `Get the code`, `Install additional build dependencies`, `Run the hooks`, `Setting up the build`를 따라함.  
단, 아래 단계들을 그대로 따라가기 위해 마지막 Setting up the build에서 `gn gen out/Debug`를 입력
## QUIC만 빌드하기
[이 링크](https://www.chromium.org/quic)를 따라가면 퀵에 관한 자세한 설명이 있음.  
위의 링크에서[Getting started with the QUIC toy client and server](https://www.chromium.org/quic/playing-with-quic)로 들어가면 QUIC Client 및 Server만 빌드하는 방법이 있음.  
