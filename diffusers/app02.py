import diffusers 
from diffusers import DiffusionPipeline as DP
from PIL import Image , ImageDraw , ImageFont

def text_to_image(text , diffuser_model) :
    # diffuser = diffuser.load_diffuser(diffuser_model)
    df = DP.from_pretrained('runwayml/stable-diffussion-v1-5' , 
                            torch_dtype=torch.float16)
    # image_data = diffuser.generate(text)
    # image = Image.fromarray(image_data)
    # image.show()
    dp = DP.from_pretrained('runwayml/stable-diffussion-v1-5' , 
                            torch_dtype=torch.float16)

    image_data = dp(text).image[0]
    image = Image.fromarry(image_data)
    image.show()

if __name__ == "__main__" :
    input_text = "Hello , World"
    diffuser_model = "example_diffuser_model"
    text_to_image(input_text , diffuser_model)