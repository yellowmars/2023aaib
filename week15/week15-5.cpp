int equalSubstring(char* s, char* t, int maxCost) {
    int ans=0,j=0;

    int N=strlen(s);
    for(int i=0;i<N;i++){
        maxCost -=abs(s[i]-t[i]);
        while(maxCost<0){
            maxCost+=abs(s[j]-t[j]);
            j+=1;
        }
        if(i-j+1>ans) ans=i-j+1;
    }
    return ans;
    
}