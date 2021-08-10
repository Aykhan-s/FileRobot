import os

class Copy_file():
    def __init__(self, file_name, walk, exception_folder, exception_files):
        self.exception_folder = exception_folder
        self.exception_files = exception_files
        self.file_name = file_name
        self.file_name_dot = '.' + self.file_name
        self.dcm = os.walk(walk)
        self.cnt = 0
        self.d = []
        self.l = ['a']
        
        self.file_search()
        
    def __file_makedirs(self, x = 1):
        try:
            os.makedirs(self.doc_address)
            
        except FileExistsError:
            try:
                os.makedirs(f'{self.doc_address}_{x}')
                self.doc_address = f'{self.doc_address}_{x}'
                
            except FileExistsError:
                x += 1
                self.__file_makedirs(x)         
        
    def file_search(self):
        
        for i in self.dcm:
            if i[0] in self.exception_folder:
                continue
            
            for k in i[2]:
                if i[0] + '\\' + k not in self.exception_files and os.path.splitext(k)[1].upper() == self.file_name_dot:
                    
                    k2 = k
                    k = k.lower()
                    
                    z = 0
                    x = 'a'
                    
                    if k in self.l:
                        splitext = os.path.splitext(k)
                        splitext2 = os.path.splitext(k2)
                        
                        while x in self.l:
                            z += 1
                            x = splitext[0] + '_' + str(z) + splitext[1]

                        x2 = splitext2[0] + '_' + str(z) + splitext2[1]
                        
                    else:
                        x2 = k2
                        x = k

                    self.l.append(x)
                    self.d.append((i[0], k2, x2))
                    
                    self.cnt += 1
        
    def file_copy(self, new_folder):
        self.doc_address = new_folder + '\\' + self.file_name
        
        self.__file_makedirs()

        for i, k, j in self.d:
            with open(f'{i}\\{k}','rb') as file:
                a = file.read()               
            with open(f'{self.doc_address}\\{j}','wb') as file:
                file.write(a)
    
    def file_delete(self):
        for i, k, j in self.d:
            os.remove(i + '\\' + k)
    
    def __len__(self):
        return len(os.listdir(self.doc_address))



class Search_file():
    
    def __init__(self, file_name, walk):
        self.file_name = file_name
        self.walk = walk
        self.l = []
        self.cnt = 0
        
    def file_search(self):
        for i in os.walk(self.walk):
             for j in i[2]:
                 if j == self.file_name:
                    self.l.append(i[0] + '\\' + j)
                    self.cnt += 1 
    
    def file_search_lower(self):
        file_name_lower = self.file_name.lower()
        for i in os.walk(self.walk):
             for j in i[2]:
                 if j.lower() == file_name_lower:
                    self.l.append(i[0] + '\\' + j)    
                    self.cnt += 1
                    
    def file_search_extention(self):
        for i in os.walk(self.walk):
             for j in i[2]:
                 if os.path.splitext(j)[0] == self.file_name:
                    self.l.append(i[0] + '\\' + j)
                    self.cnt += 1 
    
    def file_search_lower_extention(self):
        file_name_lower = self.file_name.lower()
        for i in os.walk(self.walk):
             for j in i[2]:
                 if os.path.splitext(j.lower())[0] == file_name_lower:
                    self.l.append(i[0] + '\\' + j)    
                    self.cnt += 1 
    
    def file_delete(self):
        for i in self.l:
            os.remove(i)