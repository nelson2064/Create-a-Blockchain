# Module 1 - Create a Blockchain

#To be installed:
    # Flask == 0.12.2: pip install Flask==0.12.2
    #Postman HTTP Client: https://www.getpostman.com/
    
     # Importing the libraries
    import datetime                  #datetime library is for each block have its own timestamp which is exactly date when the blok is created or min 
    import hashlib    #to hash the blocks we will work with hash funciton 
    import json               #json library becuase we will use the dom's fnction from this library  to encode the blocks before we hash them 
    from flask import Flask, jsonify #from tis flask libray we import Flask calss becuase it will create actualy an object of the flask class which will be the web application itself , #jasonify is a  function we''use to return the messages and postman when we interaact with blockahin so for ex when we make the request to get the acutal state of the blockahin to display the whole blockchain in postman well we will use jsonify  to display the response of the request and same when we mine a new blockc to add it to the blockchain  wwell we will also use jsonify  funciton to return to key informations of this new block that was just mind in the jsonify format so you willl understnand that better once we start working with jsonify but basically we will return in the json format the index of this new blog the proff of this new black  and the previous hash attached to this new block and also a little message to say that the block was just mined  
  
    