import glob
import os
import pathlib
import algorithm as wf
import pre_processor as pp

class file_bridge:
    def __init__(self,location,fileloc,report_name):
        file_search = location + '\\*.cpp'
        file_list = glob.glob(file_search)
        pre_processed_codes = []
       
        threshold = 0.3
        r_location = str(pathlib.Path(__file__).parent.absolute())
        report_location = r_location + '\\' + "Reports" + '\\' + report_name + ".txt"
        report_file = open(report_location,'w+')
        file_names = []
    
        for i in file_list:
            current_file = open(i,'r')
            file_names.append((os.path.basename(i))[:7])
            code = current_file.read()
            pre_processor = pp.pre_processing_module(code)
            pre_processor.helper()
            pre_processed_codes.append(pre_processor.s)
            current_file.close()
        
        cur_file = open(fileloc, 'r')
        cur_name = os.path.basename(fileloc)[:7]
        cur_read = cur_file.read()
        pre_cur = pp.pre_processing_module(cur_read)
        pre_cur.helper()
        cur_file.close()

        for i in range(len(pre_processed_codes) - 1):
            checker = wf.wagner_fischer(pre_cur.s, pre_processed_codes[i])
            # print(pre_cur.s, pre_processed_codes[i])
            checker.restricted_tabulation(threshold)
            plagiarism_percentage = (float)(checker.score_generator())
            plagiarism_percentage_formatted = "{:.2f}".format(plagiarism_percentage)
            str_result = cur_name + '\t' + file_names[i] + '\t' + (plagiarism_percentage_formatted) + '\n'
            report_file.write(str_result)
        
        report_file.close()