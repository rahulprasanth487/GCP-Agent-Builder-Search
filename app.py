from flask import Flask, render_template,request
import requests
import urllib.parse

app=Flask(__name__,template_folder='templates')

@app.route('/')
def handleQuery():
    return render_template('index.html')

@app.route('/handlePost',methods=['POST'])
def handlePost():
    if request.method == 'POST':
        query = request.form.get('searchQuery') 
        base_url = "https://innov-htrt-665o-1.uc.r.appspot.com/?query="
        encoded_query = urllib.parse.quote(query)
        full_url = base_url + encoded_query
        try:
            retrieved = requests.get(full_url)
            temp=retrieved.json()
            if temp["attributionToken"]:
                data = retrieved.json()
                return render_template('indexData.html', data=data, query=query)
            else:
                error = f"Error: {retrieved.status_code} - {retrieved.reason}"
                return render_template('indexData.html', error=error)
        except Exception as e:
            error = f"Error: {str(e)}"
            return render_template('indexData.html', error=error)
#         data={
#   "attributionToken": "jwHwjgoMCNWMvbIGENuRkcwCEiQ2NjRlNmEwMy0wMDAwLTI4MTktOTNhNC0wODllMDgyNWIxODgiB0dFTkVSSUMqUNuPmiLC8J4VjfenIpD3pyK3t4wt3o-aItSynRWOvp0VgLKaIvfsiC3Fy_MX-uyILYOymiLb7Ygt5O2ILavEii3e7Ygt5-2ILaOAlyKuxIot",
#   "guidedSearchResult": {},
#   "results": [
#     {
#       "document": {
#         "derivedStructData": {
#           "extractive_answers": [
#             {
#               "content": "He shows off his vocal range, hitting high notes as well as lower, more guttural tones. The lyrics are also clever and the rhymes are well thought out.",
#               "pageNumber": "20"
#             }
#           ],
#           "link": "gs://agent_builder_test/Papers/llama.pdf",
#           "snippets": [
#             {
#               "snippet": "<b>Did you know</b> that Yann LeCun dropped a rap album last year? We listened to it and here&#39;s what we thought: Dr. LeCun,&nbsp;...",
#               "snippet_status": "SUCCESS"
#             }
#           ],
#           "title": "llama"
#         },
#         "id": "0fb32bc686eb69c88c01ebe23f80706a",
#         "name": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/0fb32bc686eb69c88c01ebe23f80706a"
#       },
#       "id": "0fb32bc686eb69c88c01ebe23f80706a"
#     },
#     {
#       "document": {
#         "derivedStructData": {
#           "extractive_answers": [
#             {
#               "content": "Even though Llama 2-Chat models are capable of handling up to 4000 tokens, we limit the context and generation length to 1000 tokens to provide a fair comparison with the open-source models.",
#               "pageNumber": "56"
#             }
#           ],
#           "link": "gs://agent_builder_test/Papers/llama2.pdf",
#           "snippets": [
#             {
#               "snippet": "... <b>Llama</b> 2-Chat as the interaction model, (c) best ... Since ChatGPT, PaLM, and Falcon <b>do</b> ... If <b>you</b> don&#39;t <b>know</b> the answer to a question, please don&#39;t share false&nbsp;...",
#               "snippet_status": "SUCCESS"
#             }
#           ],
#           "title": "llama2"
#         },
#         "id": "70986183f782d7b9547c368859fece69",
#         "name": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/70986183f782d7b9547c368859fece69"
#       },
#       "id": "70986183f782d7b9547c368859fece69"
#     },
#     {
#       "document": {
#         "derivedStructData": {
#           "extractive_answers": [
#             {
#               "content": "Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023. [19] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.",
#               "pageNumber": "7"
#             }
#           ],
#           "link": "gs://agent_builder_test/Papers/llama3 quantised.pdf",
#           "snippets": [
#             {
#               "snippet": "<b>Llama</b>: Open and efficient foundation language models. ... Attention is all <b>you</b> need. Advances in neural ... Hellaswag: <b>Can</b> a machine really finish your sentence?",
#               "snippet_status": "SUCCESS"
#             }
#           ],
#           "title": "llama3 quantised"
#         },
#         "id": "1f330c02a112f996e1794f98523e5a1e",
#         "name": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/1f330c02a112f996e1794f98523e5a1e"
#       },
#       "id": "1f330c02a112f996e1794f98523e5a1e"
#     },
#     {
#       "document": {
#         "derivedStructData": {
#           "extractive_answers": [
#             {
#               "content": "Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023a.",
#               "pageNumber": "51"
#             }
#           ],
#           "link": "gs://agent_builder_test/Papers/gemini.pdf",
#           "snippets": [
#             {
#               "snippet": "<b>Llama</b>: Open and efficient foundation language models. ... <b>Can</b> ton Ferrer, Moya Chen, Guillem Cucurull, David ... Guyon, <b>U</b>. Von Luxburg, S. Bengio, H. Wal lach, R&nbsp;...",
#               "snippet_status": "SUCCESS"
#             }
#           ],
#           "title": "gemini"
#         },
#         "id": "9b5dc9d444fcba2f9891121859e32434",
#         "name": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/9b5dc9d444fcba2f9891121859e32434"
#       },
#       "id": "9b5dc9d444fcba2f9891121859e32434"
#     },
#     {
#       "document": {
#         "derivedStructData": {
#           "extractive_answers": [
#             {
#               "content": "Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023a.",
#               "pageNumber": "87"
#             }
#           ],
#           "link": "gs://agent_builder_test/Papers/gemini_v1_5_report.pdf",
#           "snippets": [
#             {
#               "snippet": "... <b>can</b> solve them. arXiv preprint arXiv:2210.09261 ... <b>Llama</b>: Open and efficient foundation language models. ... Attention is all <b>you</b> need. CoRR, abs/1706.03762&nbsp;...",
#               "snippet_status": "SUCCESS"
#             }
#           ],
#           "title": "gemini_v1_5_report"
#         },
#         "id": "122ebd3d41bb882dc415926a0ab9669e",
#         "name": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/122ebd3d41bb882dc415926a0ab9669e"
#       },
#       "id": "122ebd3d41bb882dc415926a0ab9669e"
#     }
#   ],
#   "summary": {
#     "summaryText": "## Llama: An Open-Source Foundation Language Model\n\nLlama is a family of open-source foundation language models (LLMs) known for their computational efficiency during inference. [2] This efficiency makes them well-suited for a variety of applications and deployment scenarios. [3] LLMs like Llama are trained on massive datasets of text and code, enabling them to perform a wide range of tasks, including:\n\n* **Text generation:** LLMs can generate creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.\n* **Question answering:** LLMs can answer questions based on their knowledge of the world, even in the presence of visual distortions. \n* **Multimodal question answering:** LLMs can answer questions that combine text and images, such as identifying objects in images.\n\nLlama's open-source nature allows for collaboration and customization, making it a valuable tool for researchers and developers. However, it's important to note that open-source models like Llama may not always achieve the same level of performance as closed-source models. [2] \n\nOne notable member of the Llama family is LLAMA3, which has achieved state-of-the-art performance across various tasks. [3] This performance is attributed to its massive pre-training on over 15 trillion data tokens. [3] However, quantizing LLAMA3 models can lead to performance loss, which may not be fully compensated by fine-tuning on smaller datasets. [3] \n",
#     "summaryWithMetadata": {
#       "citationMetadata": {
#         "citations": [
#           {
#             "endIndex": "272",
#             "sources": [
#               {
#                 "referenceIndex": "1"
#               },
#               {
#                 "referenceIndex": "2"
#               }
#             ],
#             "startIndex": "52"
#           },
#           {
#             "endIndex": "1069",
#             "sources": [
#               {
#                 "referenceIndex": "1"
#               }
#             ],
#             "startIndex": "925"
#           },
#           {
#             "endIndex": "1191",
#             "sources": [
#               {
#                 "referenceIndex": "2"
#               }
#             ],
#             "startIndex": "1072"
#           },
#           {
#             "endIndex": "1418",
#             "sources": [
#               {
#                 "referenceIndex": "2"
#               }
#             ],
#             "startIndex": "1192"
#           }
#         ]
#       },
#       "references": [
#         {
#           "document": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/0fb32bc686eb69c88c01ebe23f80706a",
#           "title": "llama"
#         },
#         {
#           "document": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/70986183f782d7b9547c368859fece69",
#           "title": "llama2"
#         },
#         {
#           "document": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/1f330c02a112f996e1794f98523e5a1e",
#           "title": "llama3 quantised"
#         },
#         {
#           "document": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/9b5dc9d444fcba2f9891121859e32434",
#           "title": "gemini"
#         },
#         {
#           "document": "projects/185741575305/locations/us/collections/default_collection/dataStores/ai-papers_1716443204109/branches/0/documents/122ebd3d41bb882dc415926a0ab9669e",
#           "title": "gemini_v1_5_report"
#         }
#       ],
#       "summary": "## Llama: An Open-Source Foundation Language Model\n\nLlama is a family of open-source foundation language models (LLMs) known for their computational efficiency during inference. This efficiency makes them well-suited for a variety of applications and deployment scenarios. LLMs like Llama are trained on massive datasets of text and code, enabling them to perform a wide range of tasks, including:\n\n* **Text generation:** LLMs can generate creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.\n* **Question answering:** LLMs can answer questions based on their knowledge of the world, even in the presence of visual distortions. \n* **Multimodal question answering:** LLMs can answer questions that combine text and images, such as identifying objects in images.\n\nLlama's open-source nature allows for collaboration and customization, making it a valuable tool for researchers and developers. However, it's important to note that open-source models like Llama may not always achieve the same level of performance as closed-source models. \n\nOne notable member of the Llama family is LLAMA3, which has achieved state-of-the-art performance across various tasks. This performance is attributed to its massive pre-training on over 15 trillion data tokens. However, quantizing LLAMA3 models can lead to performance loss, which may not be fully compensated by fine-tuning on smaller datasets. \n"
#     }
#   },
#   "totalSize": 370
# }
    return render_template('indexData.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
