#explore tittoken library for tokenization and encoding of text for use in OpenAI models...faster than normal tokenization and encoding methods
import tiktoken
print(tiktoken.encoding_for_model("gpt-3.5-turbo"))
encodiding = tiktoken.get_encoding("cl100k_base")
print(encodiding.encode("hi, how are you?"))
print(encodiding.decode([6151, 11, 1268, 527, 499, 30]))
text= "hi, how are you?" 
tokentext = encodiding.encode(text)
print(len(tokentext))
#pricing on tokens in openai website
