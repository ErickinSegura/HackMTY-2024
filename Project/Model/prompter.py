from openai import OpenAI

class Prompt:
    def __init__(self):
        self.client = OpenAI(api_key="-", base_url="https://fridaplatform.com/v1")
        self.absolute_path = "/workspaces/HackMTY-2024/Project/Model/Config/"
        self.file_mapping = {
            1: "ManualQuery.txt",
            2: "ManualCategorias.txt",
            3: "ManualComentarios.txt",
            4: "ManualReviews.txt",
            4: "ManualInterprete.txt",
        }

    def get_file_content(self, selection):
        try:
            file_path = self.absolute_path + self.file_mapping.get(selection, "")
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Error: The selected file was not found."
        except Exception as e:
            return f"Error: {str(e)}"

    def prompt(self, user_prompt, selection):
        setting = self.get_file_content(selection)
        if "Error" in setting:
            return setting
        
        response = self.client.chat.completions.create(
            model="tgl",
            messages=[
                {"role": "system", "content": setting},
                {"role": "user", "content": user_prompt}
            ],
            stream=False
        )
        return response.choices[0].message.content
