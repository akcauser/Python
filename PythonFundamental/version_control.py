import sys

major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]

print(major,minor,micro,sep=".")

version = sys.version

print(version[:5])

print(version.split())

print(sys.version_info)