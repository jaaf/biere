from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker, scoped_session
from database.orm_base import Base
from cryptography.fernet import Fernet
from os import path
import sys
from getpass import getpass
from shutil import which

db_name='video'
if sys.platform.startswith('linux'):
    path_to_cred=path.abspath(path.join(path.dirname(__file__),'../cred/linux'))
else:
    path_to_cred =path.abspath(path.join(path.dirname(__file__),'../cred/windows'))

try:
   
    with open(path_to_cred+'/key.bin','rb') as fileObj : 
        for line in fileObj:
            key=line
        fileObj.close() 
except Exception:
    #we could not get a key , create a new one and save it          
    key=Fernet.generate_key()
    with open(path_to_cred+'/key.bin','wb') as fileObj: 
        fileObj.write(key)
        fileObj.close()
try:
    #try to retrieve a previously saved password
    with open(path_to_cred+'/password.bin','rb') as fileObj:
        for line in fileObj:
            encrypted_password=line
        fileObj.close()
    
    password=Fernet(key).decrypt(encrypted_password).decode('utf-8')
    #print(password)
except Exception as e:
    #we could not retrieve a password create one and save it
    password=getpass("Merci de saisir le mot de passe d'administration du serveur de base de données\n")
    encrypted_password=Fernet(key).encrypt(password.encode('utf-8'))
    with open(path_to_cred+'/password.bin','wb') as fileObj:
        fileObj.write(encrypted_password)
    fileObj.close()
#check mysql server is installed
if not which('mysql') :
    print("Vous n’avez pas installé de serveur mysql. L’application ne peut fonctionner sans ce serveur. Merci de l’installer avant de continuer")
while not which('mysql'):
    pass
db_url="mysql+pymysql://root:"+password+"@localhost:3306/"+db_name
try:
    if not database_exists(db_url):
        create_database(db_url)
except Exception as e:
    end=False
    #try a new password until success
    while end==False:
        password=getpass("Merci de saisir le mot de passe d'administration du serveur de base de données\n")
        encrypted_password=Fernet(key).encrypt(password.encode('utf-8'))
        with open(path_to_cred+'/password.bin','wb') as fileObj:
            fileObj.write(encrypted_password)
        fileObj.close() 
        
        db_url="mysql+pymysql://root:"+password+"@localhost:3306/"+db_name
        #print('db_url in loop is '+db_url)
        try:
            if not database_exists(db_url):
                create_database(db_url)  
            end=True 
        except:
            print('Connexion au serveur de base de données refusée. Vérifiez le mot de passe!')  

engine = create_engine(db_url,pool_size=5,pool_recycle=3600)
Session =sessionmaker(bind=engine,expire_on_commit=False)
session =Session()


