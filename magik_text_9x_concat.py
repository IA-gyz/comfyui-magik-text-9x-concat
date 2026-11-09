class MagikText9xConcat:
    """
    Concatenate nine text strings with a configurable delimiter.
    Dynamic prompt processing is controlled by the frontend toggle.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text2": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text3": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text4": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text5": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text6": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text7": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text8": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text9": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "Enable Dynamic Prompts": ("BOOLEAN", {"default": True}),
                "delimiter": ("STRING", {"default": ",", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concat",)
    FUNCTION = "concat_text"

    CATEGORY = "Magik/text"

    def concat_text(self, text1="", text2="", text3="", text4="", text5="",
                    text6="", text7="", text8="", text9="", delimiter=",", **kwargs):
        texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
        texts = ["" if text is None or text == "undefined" else text for text in texts]
        if delimiter == "\\n":
            delimiter = "\n"
        return (delimiter.join(texts),)


NODE_CLASS_MAPPINGS = {
    "Magik_Text_9x_Concat": MagikText9xConcat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Magik_Text_9x_Concat": "Magik Text 9x Concat",
}
