from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "702157929:AAE1eD0ONdByhkJkp31kS_t_X2IPacTT-E8"
    APP_ID = 935858
    API_HASH = "6f710b2f50a55b65b7b03fb600c5e860"
    OWNER_ID = 232232522
    AUTH_CHANNEL = [-1001483488183]
    DESTINATION_FOLDER = "Tgmirrorbot" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMBNeiSHqVatY9OcLn2jMaWmDxQaKw7Ghr8GPJIIQMu0P9mgy1DWWtqhq7pXr9MTGIus8MsTOd2CTkttY9DcH2Kb4bhGpir_u3OpPjnNJ2T9mbQtYPS8KU-4vriTXkd2Jxg3IQs58_ouGjnZj5xPNNva1tX6-9w","token_type":"Bearer","refresh_token":"1//03J5h_2r5O3q0CgYIARAAGAMSNwF-L9IrgFsVY6CJWjB0LUi2hQPkTGpgGrc4iYlWVIF2sn9O2NnvnYTdFmA-v6A_Fceg0F26AeE","expiry":"2020-07-03T17:08:31.672467355Z"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
