import re

class pre_processing_module:
    
    def __init__(self,code):
        self.s = code
    
    def replacer(self,match):
            self.s = match.group(0)
            if self.s.startswith('/'):
                return " " 
            else:
                return self.s

    def comment_remover(self):
        regex_expression = r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"'
        pattern = re.compile(regex_expression, re.DOTALL | re.MULTILINE)
        self.s = re.sub(pattern, self.replacer, self.s)
    
    def define_remover(self):
        to_be_replaced = {}
        splitted_s = self.s.split('\n')

        for line in splitted_s:
            rec = line
            rec = rec.strip()
            if rec.startswith('#define'):
                line = ' '.join(line.split())
                space1 = line.index(' ')
                space2 = line.index(' ', space1 + 1)
                var = line[space1:space2]
                var = var.strip()
                org = line[space2:]
                org = org.strip()
                to_be_replaced[var] = org
            
        return to_be_replaced
    
    def define_line_remover(self):
        splitted_s = self.s.split('\n')
        edited_s = ''

        for line in splitted_s:
            line = line.strip()
            if(line.startswith('#define')):
                pass
            else:
                edited_s += line + '\n'
        
        self.s = edited_s

    
    def package_printing_remover(self):
        prog_string = self.s
        prog_line = prog_string.split("\n")
        edit_string = ""
        remove_print = "cout"
        edited_string = []
        for x in prog_line:
            x = x.strip()
            edit_string = ""
            if (x.startswith("#") and not x.startswith("#define")):
                pass
            else:
                try:
                    prog_string = x.index(remove_print)
                except ValueError:
                    edit_string = edit_string + x + ""
                else:
                    current_index = 0
                    while(current_index < prog_string):
                        edit_string += x[current_index]
                        current_index += 1
            if(edit_string != ""):
                edited_string.append(edit_string)
        self.s = ""
        for i in edited_string:
            self.s += i + '\n'
    
    def variable_changer(self):
        regex_expression = r'\w+[ \t]+(?:\*\s*)?(\w+)'
        variable_list = re.findall(regex_expression,self.s)
        cr = ''
        stopchars = set([';','\n','(',')'])
        word_end_chars = set([',','[',']',' ','=','\t','+','-','%','/','<','>','.','*','&','|','^'])
        variable_indicator = set(variable_list)
        cur_var = ''
        pcr = ''
        variables = [[],[],[],[],[],[],[],[],[]]
        updated_variable_list = []

        for i in stopchars:
            replacement = ' ' + i + ' '
            self.s = self.s.replace(i,replacement)

        for i in word_end_chars:
            replacement = ' ' + i + ' '
            self.s = self.s.replace(i,replacement)

        defines_replacer = self.define_remover()
        for i,j in defines_replacer.items():
            updated_i = ' ' + i + ' '
            updated_j = ' ' + j + ' '
            self.s = self.s.replace(updated_i,updated_j)
        
        self.define_line_remover()

        edited_s = ''
        segregated_s = self.s.split('\n')
        for i in segregated_s:
            edited_s += ' ' + i + '\n'
        self.s = edited_s

        def check_naming(name):
            if(len(name) > 0):
                if((name[0] >= 'a' and name[0] <= 'z') or (name[0] >= 'A' and name[0] <= 'Z') or name[0] == '_'):
                    return True
            return False


        def check(var,name):
            if(len(var) > 0 and check_naming(name)):
                possible_types = ['int','string','float','double','char','bool','long','short']
                bad_flags = ['return','using','#define']
                if(var in possible_types):
                    variables[possible_types.index(var) + 1].append(name)
                    updated_variable_list.append(name)
                    if(name in variable_indicator):
                        variable_indicator.remove(name)
                elif(var not in bad_flags):
                    variables[0].append(name)
                    updated_variable_list.append(name)
                    if(name in variable_indicator):
                        variable_indicator.remove(name)

        place = 0
        is_bad = False
                
        for i in self.s:
            if(is_bad):
                if(i == ')'):
                    is_bad = False
                continue
            
            if (i in stopchars):
                if(cr in variable_indicator):
                    cur_var = pcr
                if(len(cr) > 0):
                    check(cur_var,cr)
                pcr = cr
                cr = ''
                cur_var = ''
                if(i == '('):
                    is_bad = True
            
            elif (i in word_end_chars):
                if(cr in variable_indicator):
                    cur_var = pcr
                if(len(cr) > 0):
                    check(cur_var,cr)
                if(len(cr) > 0):    
                    pcr = cr
                cr = ''
            else:
                cr += i
            place += 1

        variable_indicator = set(updated_variable_list)
        count = [None,None,None,None,None,None,None,None,None]

        for i in range(9):
            count[i] = [0 for x in range(len(variables[i]))]

        for i in self.s:
            if ((i in stopchars) or (i in word_end_chars)):
                if(cr in variable_indicator):
                    for j in range(9):
                        if(cr in variables[j]):
                            count[j][variables[j].index(cr)] += 1
                cr = ''
            else:
                cr += i

        def sort_list(variable_name, variable_count):
            variable_indexes = []
            for i in range(len(variable_name)):
                variable_indexes.append(i)
            zipped_pairs = zip(variable_count, variable_indexes)
            z = [x for _, x in sorted(zipped_pairs,reverse=True)]
            sorted_variables = []
            for i in z:
                sorted_variables.append(variable_name[i])
            return sorted_variables
        
        for i in range(9):
            variables[i] = sort_list(variables[i],count[i])

        def name_replacer(var_found):
            var_name_given=['a','b','c','d','e','f','g','h','i']
            for k in range(9):
                current_counter = 1
                dict={}
                for i in var_found[k]:
                    updated_i = ' ' + i + ' '
                    dict[updated_i] = ' ' + str(current_counter) + var_name_given[k] + ' '
                    current_counter = current_counter + 1
                for i, j in dict.items():
                        self.s = self.s.replace(i, j)
        
        name_replacer(variables)
    
    def whitespace_remover(self):
        self.s = self.s.replace('\t','')
        self.s = self.s.replace(' ','')
        self.segregated_s = self.s
        self.s = self.s.replace('\n','')
    
    def helper(self):
        self.comment_remover()
        self.package_printing_remover()
        self.variable_changer()
        self.whitespace_remover()
