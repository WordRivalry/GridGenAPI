# Config that returns the path to the data directory

class Config: 
    class Paths: 
        data_dir = './data/'
        unprocessed_words_file = data_dir + 'unprocessed_words.txt'
        processed_words_file = data_dir + 'processed_words.txt'
        trie_tree_file = data_dir + 'trie_serialized.json'
        processed_word_file_analysis = data_dir + 'processed_words_analysis.json'
        model_save_path = data_dir + 'model.h5'
        weights_save_path = data_dir + 'model_weights.h5'
        grids = data_dir + 'grids.json'
        def stats_batch_file(batch_num):
            return './data/' + f'grid_{batch_num}.json'
        