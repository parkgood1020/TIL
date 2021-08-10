## 1. Docker?

- 도커는 '컨테이너 기반의 오픈소스 가상화 플랫폼'
→ 도커로 컨테이너를 띄운다.
- 그렇다면 컨테이너란?
1. 애플리케이션 & 애플리케이션을 구동하는 환경을 격리한 공간.
2. 컨테이너에 프로그램을 띄워서 구동.
3. 보통 마이크로서비스로 사용.
- 거대한 어플리케이션을 기능별로 나누어 변경/조합이 가능하게 한 것.
- 컨테이너를 사용하면 하나의 큰 어플을 서비스 단위로 잘라 빠르게 배포 가능.
- 그리고 각각 분리해서 쓰니 변경사항이 분리된 다른 기능들에 영향을 미치지 않음.

## 2. 기존의 가상머신(VM)과 컨테이너

- 기존의 가상머신(VM) 서버
- Server → Hypervisor → 각각의 Guest OS가 설치된 VM 구동.
- 가상 머신의 모든 자원을 사용.
- 컨테이너 서버
- Sever → Host OS → Docker Engine → Container 올리기.
- CPU, RAM, Disk, Network와 같은 운영체제의 자원을 필요한 만큼 격리하여 컨테이너에 할당.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65bf8545-51a2-4e3d-a885-a02dade843ab/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65bf8545-51a2-4e3d-a885-a02dade843ab/Untitled.png)

### 1) Hypervisor 가상화

 Hypervisor는 물리적인 서버 에서 하나 혹은 그 이상의 독립적인 운영체제가 돌아가는 구조이다. 즉 물리적 서버의 OS 위에 여러 다른 독립적인 OS가 가상적(virtually)으로 돌아가는 구조이다. 각각의 OS는 서로에 대해서 알지 못하며 base OS (물리적 서버의 OS)도 알지 못한다. 하나의 물리적 서버에서 실행되고 있지만 가상적으로서 완전한 독립적 OS로 운영 되는 것이다. 이러한 가상화의 장점은 물리적 서버의 리소스를 더 효율적으로 사용할수 있다는 것에 있다. 한 서버에 하나의 OS만 운영을 하는 경우 해당 OS가 서버의 모든 리소스를 항상 full로 사용하기 어려우므로 서버 리소드들이(예를 들어 CPU) idle 상태로 낭비되어 지는 경우가 있을수 있다. 

반면에 hypervisor 가상화를 사용하여 하나의 서버에 여러 OS를 실행시키면 CPU를 idle 상태로 두지않고 필요한 OS나 서비스에 할당이 되어질 수 있음으로 리소스를 훨씬 효율적으로 쓰게 되는것이다. 그럼으로 고급 사양의 좋은 서버에 여러 가상화 OS들을 운영하는 것이 저급이나 중급 사양의 여러 서버를 운영하는것보다 훨씬 효율적이라는 것이다. 단점은 기술적을 너무 무겁다(heavy-weight)는 것이다. 독립적인 OS를 실행시키는 것이기 때문에 booting 시간이 길 수 밖에 없으며 리소스를 많이 차지할수 밖에 없다.

### 2) Container 가상화

 Docker 같은 컨테이너 가상화 기술은 hypervisor 가상화와 다르게 OS의 커널 위의 유저 공간(user space)에서 실행된다. 즉 완전히 독립적인 운영체제를 가상화 하는 것이 아니라 독립적인 user space를 가상화 한다고 생각하면 쉽다. 즉 하나의 호스트 서버에서 여러 독립적인 user space 인스턴스들을 가상적으로 실행할 수 있게 되는 것이다. 이러한 가상화 기술의 장점은 hypervisor 가상화 보다 훨씬 가볍기 때문에 빠르고 쉽게 독립적인 가상 환경을 실행시킬수 있다 (또한 hypervisor는 base OS와 가상화 OS 사이에 커널 시스템 호출을 연결 시켜주는 emulation layer가 필요한데 docker는 hypervisor 처럼 emulator가 필요없이 그냥 일반적인 시스템 API interface를 사용한다). 

예를 들어 docker image만 있으면 어디서든 쉽고 빠르게 test 환경, sandbox 환경 및 production 배포를 할 수 있다. 그럼으로 최근에 널리 퍼져있는 MSA(Micro Service Architecture)와 CI/CD에 아주 잘 어울리는 가상화 기술로서 각광을 받고 있다. 단점은 독립적인 OS가 아닌 user space 가상화를 하는 형태이다 보니 운영체제가 전혀 틀린 호스트에서는 실행을 시킬수가 없다. 예를 들어 Windows 를 linux 호스트에서 실행시킬수 없다.

(하지만 사실 개발자라면 windows는 어차피 대부분 사용 안할테니 크게 상관없다). 그리고 완전히 독립적인 운영체제 가상화가 아니다 보니 보안적인 측면에서 hypervisor 보다 약할수 밖에 없다.

## 3. 특징

**독립적이고, 동적이다.**

- 앱의 사용량에 따라 앱 컨테이너의 수를 늘리고, 다시 트래픽이 줄면 해당 컨테이너 수를 줄일 수 있음.
- 즉, docker 덕분에 매번 새로운 서비스를 만들 때마다 새로운 서비스를 사고, 설정할 필요가 없음. 원할 때마다 docker를 통해 새로운 환경을 생성할 수 있음.
- 하나의 같은 서버에서 각기 다른 환경의 컨테이너를 설정할 수 있고, 게다가 이 컨테이너들은 각각 분리, 독립되어 있는 것이기 때문에 더욱 효율적.

## 4. 구조

Docker는 크게 4가지로 구분.

- Docker client와 server (server는 docker engine으로 불리기도 함)
- Docker 이미지
- Docker registries
- Docker containers

### 1) Docker client 와 server

Docker는 클라이언트 와 서버 구조로 이루어저 있다. 클라이언트가 서버에 명령을 전달하고 서버가 실행시키는 구조이다. docker binrary 커맨드가 docker 클라이언트 이고 dockerd 가 docker daemon 혹은 docker engine이다. Docker engine과 interact하기 위한 Restful API도 제공된다. 클라이언트와 서버는 동일한 호스트 안에서 운영 될수도 있으며 서로 다른 호스트에서 운영 될수도 있다.

### 2) Docker 이미지

Docker의 life cycle에서 docker 이미지는 “build”의 부분에 해당된다. Docker container에서 실행시키고 싶은 application을 docker 이미지로 빌드해서 실행시키게 된다.

### 3) Docker registries

Docker registires는 docker 이미지를 저장하는 repository라고 보면 된다. Source code를 github에 저장하여 관리하듯 docker 이미지는 dockerhub 같은 docker registries에 저장한다고 생각하면 된다. Github가 마찬가지로 public registry 가 있고 private registry가 있다.

### 4) Docker containers

Docker container에서 docker 이미지가 실행된다. 즉 docker 이미지를 실행시키는 가상화 공간 이다. Docker container는 하나 혹은 그 이상의 프로세스를 실행 시킬수 있다 (하지만 하나의 프로세스만 실행시키는 것을 권장).

### 5) Docker Compose And Swarm

Docker에서는 여러 docker container들로 이루어진 stack이나 cluster를 관리 하는 서비스도 제공하는데 바로 docker compose 와 docker swarm이다.

**Docker compose는 복수의 docker container들을 모아서 종합적인 application stack을 정의 하고 운영할수 있도록 해주는 서비스**이다. Compose 파일을 사용하여 전체적인 application 서비스를 설정한후, application을 이루고 있는 각각의 컨테이너들 (예를 들어, web 서버 컨테이너, api 서버 컨테이너 등등)을 따로 실행시킬 필요 없이 한번에 생성하고 실행할 수 있도록 해준다. **Docker swarm은 docker containers 들로 이러우진 cluster를 관리할수 있도록 해주는 서비스**이다. 즉 docker container를 위한 clustering tool 이다.

## 5. Docker Compose

- **다중 컨테이너 애플리케이션을 정의, 공유**할 수 있도록 개발된 도구로 **단일 명령을 사용하여 모두 실행 또는 종료** 할 수 있도록 개발된 도구.
- compose는 프로젝트 이름을 사용하여 환경을 서로 격리하고 여러 다른 콘텍스트에서 이 프로젝트 이름을 사용하여 접근함.

