from os import scandir as DirScanner
from os.path import abspath
from os import getcwd
from collections import defaultdict
import subprocess

class ExceptionBinDir(Exception):
    pass

class ExceptBasedir(Exception):
    pass

def shell_caller(cmd, encoding = "utf-8"):
    def caller(*args, to_stdout = False):
        ret = subprocess.run([cmd, *args],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if encoding:
            if ret.stdout:
                ret.stdout = ret.stdout.decode(encoding)
            if ret.stderr:
                ret.stderr = ret.stderr.decode(encoding)

        if ret.returncode != 0:
            if to_stdout:
                print("ERR: ")
                if ret.stderr:
                    print(ret.stderr.decode("utf-8"))
            return ret
        if to_stdout:
            print(ret.stdout.decode("utf-8"))
        return ret

    return caller

class CmdCallRet:
    def __init__(self, returncode = 0, out = None, err = None):
        self.stdout = out
        self.stderr = err
        self.returncode = returncode

class ShellCmder:
    def __init__(self, bin_dir = "/bin"):
        self.cwd = getcwd()

        if not self.__is_abs_path(bin_dir):
            bin_dir = self.__get_abs_path(self.cwd, bin_dir)

        self.bin_dir = bin_dir
        self.commands = defaultdict(lambda : None)

        self.__scan_bin(self.bin_dir)

    def __get_abs_path(self, base, append):
        if not self.__is_abs_path(base) :
            raise ExceptBasedir("base dir need to be abs path.")
        return abspath(base + "/" + append)
    
    def __is_abs_path(self, path):
        return path.startswith("/")

    def __scan_bin(self, path):
        try:
            scanner = DirScanner(path)
        except Exception as e:
            print(e)
            raise(ExceptionBinDir)

        for entity in scanner:
            if  entity.is_file:
                cmdpath = self.__get_abs_path(self.bin_dir, entity.name)
                self.commands[entity.name] = shell_caller(cmdpath)

    def __getattr__(self, k):
        if k not in self.commands:
            return lambda *args : CmdCallRet(returncode = 1, err = "cmd: '{}' not defined in bin: '{}'".format(k, self.bin_dir))
        return self.commands[k]

    @staticmethod
    def is_ok(ret):
        return ret.returncode == 0

    @classmethod
    def show(cls, ret):
        if cls.is_ok(ret):
            if ret.stdout:
                print(ret.stdout)
        else:
            if ret.stdout:
                print(ret.stdout)
            if ret.stderr:
                print(ret.stderr)

if __name__ == "__main__":
    cmder = ShellCmder("./bin/")
    ret = cmder.sum(1,2,3,4)
    cmder.show(ret)

