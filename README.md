# LangChain X OpenAI - Bring your own data

> **Note**: Currently, it only supports markdown & txt files. Maybe in the future, I will support more file types (like pdf, docx, xls, etc.)

## How to use

> **Note**: Add the `OPENAI_API_KEY` to your [environment variables](https://gitpod.io/user/variables) in the Gitpod dashboard OR in the `.env` file.

1. Open in Gitpod, then you don't need to install anything on your local machine.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Siddhant-K-code/OpenAI-bring-your-own-data)

2. You can add your own data in the `data` folder. You can add multiple files in the `data` folder. The more data you add, the better the model will be. Currently, it only supports markdown & txt files.

3. Run the following command:

   ```bash
   pyenv virtualenv 3.9.9 fun_openai_work
   pyenv activate fun_openai_work
   python server.py
   ```

4. Open the url that is generated in the terminal. It will look something like this: `http://127.0.0.1:5000/`

5. Ask your question with:

    ```
    http://127.0.0.1:5000/chat?question="something about siddhant"
    ```
    
    Output:
      <img width="1000" alt="image" src="https://user-images.githubusercontent.com/55068936/230473879-c3ffc84c-fb2d-44fc-8a32-a5b063ce47a3.png">


> **Note**: if you want to rebuild your db, just delete the "checkpoint" file. It will rebuild the db from scratch. And, then you can run the server again.
