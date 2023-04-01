from pytube import YouTube
def download_vdo(lnk):
    getOnYt=YouTube(lnk)
    print('finding all streams...')
    vdoTypes=getOnYt.streams
    allStreamsInList=list(enumerate(vdoTypes))
    for i in allStreamsInList:
        print(i)
    ch=int(input('enter your choice : '))
    print(f"{getOnYt.title} \nsdownloading...")
    vdoTypes[ch].download()
    print('Download succussfully')

    
    
