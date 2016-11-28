import os
import Code_Review_Assigner.parse_git_log as pgl
import unittest
import Code_Review_Assigner.commitHistory as ch

class TestParseMethods(unittest.TestCase):

    def test_getPreviousCommitsInTree(self):
        previous_count_by_guid = {}
        previous_count_by_guid['f8d7ae9b079f2a65701cac73d58d1d168e40c7cf'] = 0
        previous_count_by_guid['ff7c23a3d5bc57f887dfab038a2c98243efded56'] = 1
        previous_count_by_guid['1c818f6d777ab9302d3086008b4e1ab78878f80a'] = 2
        previous_count_by_guid['104c11dede8944b56a2413b7e74117eb352de410'] = 3
        previous_count_by_guid['d98c2aa936fba01d45a66d2eb614217c5f7355fb'] = 4
        previous_count_by_guid['7f00845dff682181ab551f30e92663fcb0c22976'] = 5
        previous_count_by_guid['69e551585a25b5ece2fb519b280a375a5f8ae51e'] = 6
        previous_count_by_guid['7614e7d72bc552a73cfb3cdf65c88b6ea9ba844e'] = 7
        previous_count_by_guid['4e7c12551475aa9b465cedabcdf4a46ed1042936'] = 8
        previous_count_by_guid['ace7b33285e534ebbad54037b694087192c694ce'] = 9
        previous_count_by_guid['43f6c69eed3ad19e621bf4b42c17cca62f552b6d'] = 10
        
        testHistory = pgl.parse(os.getcwd() + '\\samplerepo\\')
        for c in previous_count_by_guid:
            prevCount = testHistory.get_previous_commits(c)
            self.assertEqual(len(prevCount), previous_count_by_guid[c])

    def test_getCommitsInTree(self):
        commits_in_tree_by_guid = {}
        commits_in_tree_by_guid['f8d7ae9b079f2a65701cac73d58d1d168e40c7cf'] = 0
        commits_in_tree_by_guid['ff7c23a3d5bc57f887dfab038a2c98243efded56'] = 1
        commits_in_tree_by_guid['1c818f6d777ab9302d3086008b4e1ab78878f80a'] = 2
        commits_in_tree_by_guid['104c11dede8944b56a2413b7e74117eb352de410'] = 3
        commits_in_tree_by_guid['d98c2aa936fba01d45a66d2eb614217c5f7355fb'] = 2
        commits_in_tree_by_guid['7f00845dff682181ab551f30e92663fcb0c22976'] = 4
        commits_in_tree_by_guid['69e551585a25b5ece2fb519b280a375a5f8ae51e'] = 5
        commits_in_tree_by_guid['7614e7d72bc552a73cfb3cdf65c88b6ea9ba844e'] = 5
        commits_in_tree_by_guid['4e7c12551475aa9b465cedabcdf4a46ed1042936'] = 6
        commits_in_tree_by_guid['ace7b33285e534ebbad54037b694087192c694ce'] = 7
        commits_in_tree_by_guid['43f6c69eed3ad19e621bf4b42c17cca62f552b6d'] = 10
        
        testHistory = pgl.parse(os.getcwd() + '\\samplerepo\\')
        for c in commits_in_tree_by_guid:
            treeCount = testHistory.get_commits_in_tree(c)
            self.assertEqual(len(treeCount), commits_in_tree_by_guid[c])

if __name__ == '__main__':
    unittest.main()