# Module 1 - Create a Blockchain

#To be installed:
    # Flask == 0.12.2: pip install Flask==0.12.2
    #Postman HTTP Client: https://www.getpostman.com/
    
    
    # Importing the libraries
    import datetime                  #datetime library is for each block have its own timestamp which is exactly date when the blok is created or min 
    import hashlib    #to hash the blocks we will work with hash funciton 
    import json               #json library becuase we will use the dom's fnction from this library  to encode the blocks before we hash them 
    from flask import Flask, jsonify #from tis flask libray we import Flask calss becuase it will create actualy an object of the flask class which will be the web application itself , #jasonify is a  function we''use to return the messages and postman when we interaact with blockahin so for ex when we make the request to get the acutal state of the blockahin to display the whole blockchain in postman well we will use jsonify  to display the response of the request and same when we mine a new blockc to add it to the blockchain  wwell we will also use jsonify  funciton to return to key informations of this new block that was just mind in the jsonify format so you willl understnand that better once we start working with jsonify but basically we will return in the json format the index of this new blog the proff of this new black  and the previous hash attached to this new block and also a little message to say that the block was just mined  
  
    
  # Part 1 - Building a Blockchain      
                                       #how we are going to build blockchain there are several option first option would bet to  make several function and use afterwards to function to build a blockchain and this is not the best option and this shuldn't be the mindset the  devloper should have when building somehting huge  blockchain is huge it supposed to be decentralized network that is all over the world with tons of  blocks min  one after other and that not the bst way to build        the best way tot build a kind of stystem is with a class you can build anything with a class  you can build self driving car whatever you want and the reason fo rhti sis because a clas sbascally contians some advanced structure in which you can include property function tools methods all of them interacting with what you wnat to build
   
  class Blockchain:
      
      df _init_(self):
          #initalize chain that contains block 
          self.chian = 
      
  

                
      
                        # Module 1 - Create a Blockchain

                        # To be installed:
                        # Flask==0.12.2: pip install Flask==0.12.2
                        # Postman HTTP Client: https://www.getpostman.com/

                        # Importing the libraries
                        import datetime
                        import hashlib
                        import json
                        from flask import Flask, jsonify

                        # Part 1 - Building a Blockchain

                        class Blockchain:

                            def __init__(self):
                                self.chain = []                                           #let's initialize our blockchain so to do this we will need to init the chain that will contian the blocks // this will be simply the chain in the blockchain and this will be simply be a list continaing the differnet blocks initlaize list  
                                self.create_block(proof = 1, previous_hash = '0')         #the other mendatory thing that we have to do to init our blockchain is to create the  genesis block the genesis block is the first block of the blockchain to crate it we're going ot use a fucntion that will make in the next tutorial and that we'' call the creat block method  so to create this genesys block the  first blockc of the blockchain i am gona call the future funciton that will make which is creatblock first arugument is proof  becuase each block of the blockchain have its own proof and here we can choose an arbitary value and   so the common pracise is to start with 1 a proof of one   seond arugment is previous hash the link with previous hash so this is the first block so previous hash is 0  >> now lets create creat_block function not reall to get this genesys block but also to be able to creat ehe next blocks once thery are mint  #differnece between the create_block function that we're about to make and the future_min block function that we will build at the end of this module adn the differnece to understnad is ttha we applyy create_block fucntion right after mining a block the min block funciton will simply get the proof of work that we all need to solve so we will define the problem and we will define the algorithm to find that work and then once we find this proof of work then that means a new block is mine   and that's when we can create a new block and added to th4e blockchain //so this new create block funciton that we're about tomake will not only create the block with all the differnet features like the index , the timestamp , the proof , and the previous hash , but also will appended this new min block to the blockchain 




                            def create_block(self, proof, previous_hash):            # create a block and add to the blcockhain  #
                                block = {'index': len(self.chain) + 1,                #length of a chain and add 1 with every blockchain           #make a dictionary that will define each block in the block chain with its four essential keys #first essential keys is index of the block then seond the timestamp  it is the exact time when the block is min then third the proof of the block which is to prove that was fine when ming this new block  and eventually the previous hash but you can actually add anythign else anythign you want inside theis dictionary and thats exactly what we'll will do and this module 2 in this module will add some dat in this block that will be the transactionso of the cryptocurrencyt that will make and that i remind is god had coin  and so this is to show you that right now we are creating a genearl blockchain in which you can add anthing in a nuki that you could call dataall right so le'ts include these four keys and then we'll simply append htis new block to the blcockhain 
                                         'timestamp': str(datetime.datetime.now()),   #exact time when block is mine #to get this time we use datetime library that will give us exactly the year the month the day hour the minutes and the seconds when the block is min #we need to put that in a stirng a string otherwise we will have some format issue when working with json format
                                         'proof': proof                               #the proof that we got when mining the block by solving proof of work
                                         'previous_hash': previous_hash               #previous hash 
                                         #'data':                                     #if you want to add any data inside the block so right now we are creating a general plain block chain  and in the next moudle we'll add some data which will be the transactions o the cryptocurrency to add some data in the blockchain you can simply add a new key here would be for exmaple data and attached to this key you can include anything we are doing in this module 1 because we are creating a general blockahin and we will gona use these four key which define a block in our blockchain  
                                         }               
                                self.chain.append(block)                               #now we have block now we have to simply append to our chain so chain is a list so to append this block we use append
                                return block                                            #retrun the block becuawse we gona display information of this block in postman an dby information means off course these four keys
                            
                            
                            

                            def get_previous_block(self):                                 #get the last block    
                                return self.chain[-1]                                     # chain -1 is the last block of the chain 



                        #what is proof of work ? so a proof of work  is the number or piece of data that the miners have to find in order to mine a new block  so we're going to define a problem and the miner have to solve that problem and to solve this problem they have to find the specify number that will be exactly this proof of owrk and tha tiwll be this proof arguments expected by the creat_block function #so we'll define a problem that willl be challlenging to sovle but eays to verify and that's the principle that's the key point to understand baou the proof of work it's a number that is hard to find but easy to verify  why does it have to be hard to find that  becuase if it was easy to find  well miners could easily mined tons of blocks and for example ex if you blockhain holds a cryptocurrency well the miners could easily get tons and tons of cryptocurrency and therfore since it si easy to get it hass less value we we have to make it hard to get for it not to lose its value  and why does it have to be easy to vgerify that bucause when a miner solves the problem and finds a potential proof of owrk well the other miners need to verify that indeed the first miner to solve the problem and so that's exactly what they will implement in this proof of work funciton 
                            def proof_of_work(self, previous_proof): #fist argument self aoff course becuase we will apply this proof of owrk method from   the instance object that will be created from the class but then there is another argument which    is previous proof because in order to make the problem that the miners will hae to solve will take take into account the previous proof      so in other owrds the previous proof is an element of the problem that the miners will need to counter  to find the new proof         #defining a problem that the miner have to solve to mine a block we will defina a problem so this proof of work fucntion reutrn proof this is the fucntion that the miner have to execute to find the proof and at the last we return the proof and this will be exactly the proof that we need here to creat a new block with also the previous hash but whihc we already have thanks to the last block which we can get thanks to this get previous block method that we just made lets' do this 
                                new_proof = 1               # we initialize it to 1 that's becuase to solve the problem we're going to increment this new proof by one at each iteraiton of a while loop unitl we get the right proof so basically wer're solving tyhe problem with a tril and error approach ok so new proof is staring at 1 
                                check_proof = False    #then just before we atrt this while loop to increment this new proof and chekc if it is thte right proof 
                                while check_proof is False:       # until check_proof is false we run this loop we will iterate try fial then 
                                    hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()  #use hashlib libary and take sha256 cryptographic hash fucntion   and that's where we input the operaiton of the  previous proof and the new proof and what is this operation going to be it will be non symmetriacal so for ex we cannot take new proof plus previous proof   new_prrof + previous_proof because new proof plus previous proof equals previous proof plus new proof  adn therefore since we incrememtn new proof  at some point the new proof will become an old previous proof you will be able to chekc that hwen runnign the plugs you will ee that you will have the same proof every two blocks and thath's only because the operation is symmetrical so in order to make that operaiton non symmetrical we cna ismply take for ex the operation new  pfoof minus  previous proof  because new proof minus prvious proof is not equal to previous proof minus new proof and therefore that works    but new_prrof-prvious_proof    but   this is too simple   we're going to make that slightly more challenging but not to challenging so im' just going to add  square here and squeare so we can take square new poff - square of prvious proof but still this is still easy you can practise even more complex and the problem more challenging     and now to make thi acceptable we simply need to add some code that will give us the right formaat tha tis expoerted by 256 funciton   fist convert in sting fucntion and then add encode        and the encode fucniton will encode the string and in right format which is exported by sha256 function       so encode fucntio nwill do is you can chek in console               #the problem that the miners will have to solve //so what is this problem going to be so we gona usse the hash fucntion we're going to use the sha 256 cryptographic hash funciton combined to the hex digit funciton to return a sting of 64 characters and this string will need to start with what we call four leading zeros the leading zeros id is a classic way of definig a problem that th eminers have to solve to find the proof of work and the key thing to understand here is tha tthe more leading zeroes you impose the hardet it wil be for miner to solve the problem so we're not oging to too many little zeros becuase i winat you to mine th eblocks versy easily we're not making a real cryptocurrrency tha tiwll be traded all around the world today is just for educational purposes so we'l mak a simple proof of owrk with falling zeros and we;'re gong ot start by intoducing a new varaibel hash_operation 
                                    if hash_operation[:4] == '0000':#the first four indexes of this hash opeartion which a string of 64 characters so we're going to take  first four so to take the first four index if first four index is 0 then the miner wins and check proof = true but if the minor loses if the minor cannot find this in that case else he looses and chek proof kept to false and we give other chance to minor   #checking if the fist four charcters of this hash operation are four zeros thats the four zero i am talking about if thsese first four charcters of four zeros well we win well the minor wins and check check proof will be set true and the new proof will be returned that is this new proof giving us the result of a cryptographic hash starting with four zeros will be the proof accepted to mine a new block 
                                        check_proof = True
                                    else:
                                        new_proof += 1
                                return new_proof     #if first four index is 000 and if true then we will return new_proof 
                            
                            
                            #it's a function that will check if everyghing is right in our blockchain and everyhing is right i mean we're going to chekc two essential things rist we're going to chek if each block in the blockchain has a correct proof of work that is has a proof of owrk that solved this problem by returning a cryptographic hash that starts with four leading  zeros and then the second thing we're going to chekc is that the previous hash of each block is equal to the hash of the previous block and by checking thsese two things that means that we'll have a valid block chain and so that's the final thing we need to do here make that two function
                           #function to check everything is right in our blockchain we gona check two essential thing > if each block in the blockchain has a correct proof > another things is previous hash of each block is equal to the hash of the previous block by checking this two things means that we have a valid blockchain 
                           #final thing we need to do here 
                           def hash(self, block):       
                                encoded_block = json.dumps(block, sort_keys = True).encode() # we are encoding our block in right format so it can be accepted by sha256 hash funtion first our block sort keys argumaent whcih will set equsl yo true so that our block dictionary is sorted by keys   #each block of blockhcian has dictionoary with four key but first thing we need to do exactly as do is make this deictionary a string we gona use json libary from this json libary we use dom function that exactly tyaksa an object and makes a string > why we take dom funciton from json libary not directly becuase in part two we will put our blocks dictionaries into a json file you know in the json format and therefore our blocks originally in a dictionary will have to json format and we tak dom from json to make our dictionary stirng 
                                return hashlib.sha256(encoded_block).hexdigest()     #hexdigest is used to get in hexadecimal format now we have hash function that reutrns a cryptographic hash  of our block  
                            
                            
                            
                            #is chain valid funciton that will chek our blockchain is valid 
                            #first chek that the previous hash of each block is equal to the hash of its previous block 
                            #second thing will chek is that the proof of each block is valid according to our proof or work problem that we defined in this proof_of_work fucntion 
                            def is_chain_valid(self, chain):
                                previous_block = chain[0]
                                block_index = 1
                                while block_index < len(chain):
                                    block = chain[block_index]
                                    if block['previous_hash'] != self.hash(previous_block): #is the current block previous hash is not equal to the previous block its hash then return false
                                        return False
                                    previous_proof = previous_block['proof']     #previous block proof
                                    proof = block['proof']              #current block proof 
                                    hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()           
                                    if hash_operation[:4] != '0000':         #checking if the first 4 four index of hash operaiton is 0 if not then return false 
                                        return False
                                    previous_block = block   #    the current block will be the previous block when new block will came so new block will came if it pass all chek of is_chain_valid           
                                    block_index += 1           #increment the block index 
                                return True      #if everyhging gone well we return true 
                            
                            
                            
                            #congraturlation for  building arcitecture of our blockhain
                            
                         
                        # Part 2 - Mining our Blockchain

                        # Creating a Web App
                        app = Flask(__name__)

                        # Creating a Blockchain
                        blockchain = Blockchain()

                        # Mining a new block
                        @app.route('/mine_block', methods = ['GET'])
                        def mine_block():
                            previous_block = blockchain.get_previous_block()
                            previous_proof = previous_block['proof']
                            proof = blockchain.proof_of_work(previous_proof)
                            previous_hash = blockchain.hash(previous_block)
                            block = blockchain.create_block(proof, previous_hash)
                            response = {'message': 'Congratulations, you just mined a block!',
                                        'index': block['index'],
                                        'timestamp': block['timestamp'],
                                        'proof': block['proof'],
                                        'previous_hash': block['previous_hash']}
                            return jsonify(response), 200      #return in json format 

                        # Getting the full Blockchain
                        @app.route('/get_chain', methods = ['GET'])
                        def get_chain():
                            response = {'chain': blockchain.chain,
                                        'length': len(blockchain.chain)}
                            return jsonify(response), 200

                        # Checking if the Blockchain is valid
                        @app.route('/is_valid', methods = ['GET'])
                        def is_valid():
                            is_valid = blockchain.is_chain_valid(blockchain.chain)
                            if is_valid:
                                response = {'message': 'All good. The Blockchain is valid.'}
                            else:
                                response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
                            return jsonify(response), 200

                        # Running the app
                        app.run(host = '0.0.0.0', port = 5000)
