def main():
    for i in range(100):
        page = i+1
        f = open(str(page)+".txt","w+")
        f.write("This is page %s." % (page)  )
        f.write("\rThis is where your amazing writing with go."  )
        f.close()

if __name__ == "__main__":
    main()
