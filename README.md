# Terminal Groq

This repository is forked from https://github.com/tomwarias/Terminal-Groq-Chat 该贡献者提出了一种在命令行调用Groq的API展开多轮对话的prompt界面，就像这样：

```sh
>>> User: 
<<< Jarvis: 
```
运行Terminal-Groq-Chat的代码需要在其项目目录下使用`python3 groq.py`命令，而无法随时随地使用`tgroq`运行，也不能像这样`tgroq "My Question is..."`

However, 我做了以下改进：
1. rename `groq.py`为`tgroq` 以避免`import groq`和自身文件名的冲突
2. 修改代码使得可以直接将问题作为参数以运行`tgroq "My Question is..."`
3. 编辑了`tgroq.sh`并添加到环境变量以随时随地调用`tgroq`呼出
4. 保留了多轮对话机制。当无参调用`tgroq`时，开始多轮对话，当使用`tgroq "My Question is..."`时，直接将回答输出到终端


### Installation Steps

1. **Clone the Repository**

    ```sh
    git clone https://github.com/AWSzyAI/tgroq.git
    ```

2. **Install Dependencies**

    Set API key, you can found it here https://console.groq.com/keys:

    ```bash
    set GROQ_API_KEY=<your_api> 
    ```
    
3. **Install Dependencies**

    Install the necessary Python packages by running:

    ```bash
    pip install groq, asyncio
    ```

4. add tgroq to PATH

    ```sh
    chmod +x init.sh
    sudo ./init.sh /usr/local/bin/
    ```

5. **Run the Application**

    Start the code with:

    ```bash
    tgroq
    tgroq "Your question"
    ```
