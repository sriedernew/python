def main(): 
    try:
        f = open("große_paddelei.txt","r")
    except (OSError,IOError) as err:
        print("Error: {}".format(err))
    except:
        print("was anderes")
    else:
        print("alles gut")
    finally:
        print("das war f open")

   
if __name__ == "__main__":
  main()