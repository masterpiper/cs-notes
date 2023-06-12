```toc
```

## Introducation
The nature of spider is a programing which *stimulate browse web* and *catch data from the Internet*.

## Legally Rules
- **Dont prevent normal operating of the web**.
- **Dont catch the protected data and information**.
- Check the content which you catched, and insure that dont include sensitive information.
## Spider Basic
### Classification

#### Universal Crawler
- Catch a whole page.
```mermaid
graph LR;
subgraph Requests basic flow
	step1[GET URL]-->step2[Send Requests]
	step1-->step5[UA Disguise]-->step6[Set Params]-->step2
	step2-->step3[GET responded data]
	step3-->step4[Store]
 end

```
#### Focused Crawler
- Base on universal crawler.
- Catch local data from the whole page.
```mermaid
graph LR;
step1[Set URL]-->step2[Request]-->step3[Get data]
step3-->step4[Analysis]-->step5[Storage]

```
#### Incremental Crawler
- Monitor website updates, and catch the updates.

### Anti-crawling mechanism
#### Robots protocal
This protocal stipulate the data  enable catched.
Browse `www.taobao.com/robots.txt`, you can find the robots protocal.
### Anti-anti-crawling mechanism

## Web Basic
### Http & Https
```Request Header
User-Agent: Requester's identification.(include OS version, Browser version)
Connection: State of connection when after get request.(KEEP or ALIEVE)
```

```Respond Header
Content-Type: the data type when server respond to the client.
```
(PS:https meas security http. Tttps use data encryption.)

#### Data encryption
- Symmetric key encryption: The Client formulates the encryption method and sends the decryption method to The Server.
- Asymmetric key encryption: The Server formulates the encryption method and tell the client. When Client send the message to Server, it must use the encryption method.
- Certificate-key encryption(HTTPS): 

## Programing
```python
url = "www.baidu.com"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
```

### Create Request
```mermaid
flowchart TB
	subgraph Catch_pakage
		direction LR
		r1[catch request]-->r2[get UA and URL]
	end
	subgraph Create_request
		direction LR
		r3[Set Header and UA]
		r3-->r4[Set HTTP Mothed]
	end
	Catch_pakage-->Create_request
```

```python

```
### Analysis data
```mermaid
flowchart TB

```
