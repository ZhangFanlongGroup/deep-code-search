
def config_JointEmbeder():   
    conf = {
        # data_params
        'dataset_name':'CodeSearchDataset', # name of dataset to specify a data loader
            #training data
            'train_name':'train.name.h5',
            'train_api':'train.apiseq.h5',
            'train_tokens':'train.tokens.h5',
            'train_desc':'train.desc.h5',
            #test data
            'valid_name':'valid.name.h5',
            'valid_api':'valid.apiseq.h5',
            'valid_tokens':'valid.tokens.h5',
            'valid_desc':'valid.desc.h5',
            #use data (computing code vectors)
            'use_codebase':'use.rawcode.txt',#'use.rawcode.h5'
            'use_names':'use.name.h5',
            'use_apis':'use.apiseq.h5',
            'use_tokens':'use.tokens.h5',     
            #results data(code vectors)            
            'use_codevecs':'use.codevecs.normalized.h5',#'use.codevecs.h5',         
                   
            #parameters
            'name_len': 6,
            'api_len':30,
            'tokens_len':50,
            'desc_len': 30,
            'n_words': 10000, # len(vocabulary) + 1
            #vocabulary info
            'vocab_name':'vocab.name.json',
            'vocab_api':'vocab.apiseq.json',
            'vocab_tokens':'vocab.tokens.json',
            'vocab_desc':'vocab.desc.json',
                    
        #training_params            
            'batch_size': 64,
            'chunk_size':200000,
            'nb_epoch': 10,
            #'optimizer': 'adam',
          #  'learning_rate':1e-4,
          #  'adam_epsilon':1e-8,
          #  'warmup_steps':5000,

        # model_params
            #'emb_size': 512,
            #'n_hidden': 1024,#number of hidden dimension of code/desc representation
            # recurrent
            #'lstm_dims': 512, # * 2          
            #'margin': 0.5,
            #'sim_measure':'cos',#similarity measure: gesd, cosine, aesd
         
    }
    return conf




