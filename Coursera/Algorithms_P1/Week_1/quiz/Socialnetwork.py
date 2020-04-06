"""
 * Coursera - Algorithms Part I
 * Week 1 - Interview Questions - Union Find
 *
 * Question 1: Social network connectivity
 *
 * Given a social network containing N members and a log file containing M
 * timestamps at which times pairs of members formed friendships, design an
 * algorithm to determine the earliest time at which all members are connected
 * (i.e., every member is a friend of a friend of a friend ... of a friend).
 * Assume that the log file is sorted by timestamp and that friendship is an
 * equivalence relation. The running time of your algorithm should be MlogN or
 * better and use extra space proportional to N.
 */"""

"""
/**
 * Solution:
 *
 * Use a union-find data structure with each site representing a social network
 * member. Add unions between sites in time order of friendships being formed.
 * After each union is added, check the number of connected components
 * within the union-find data structure. If only one, all members are connected.
 *
 * Must keep track of number of unique components. Decreases when a union occurs
 * between different components.
 */
"""

"""
The assumption that the log file will look something like this:
0 1 2015-08-14 18:00:00
1 9 2015-08-14 18:01:00
0 2 2015-08-14 18:02:00
0 3 2015-08-14 18:04:00
0 4 2015-08-14 18:06:00
0 5 2015-08-14 18:08:00
0 6 2015-08-14 18:10:00
0 7 2015-08-14 18:12:00
0 8 2015-08-14 18:14:00
1 2 2015-08-14 18:16:00
1 3 2015-08-14 18:18:00
1 4 2015-08-14 18:20:00
1 5 2015-08-14 18:22:00
2 1 2015-08-14 18:24:00
2 3 2015-08-14 18:26:00
2 4 2015-08-14 18:28:00
5 5 2015-08-14 18:30:00
"""

"""
class MyClas {
    private int[] a;
    private int[] size;
    int N=0;
    public MyClas(int n){
        N=n;
        a = new int[n];
        size = new int[n];
        for(int i=0;i<n;i++){
            a[i]=i;
            size[i]=1;
        }
    }
    private int root(int x){
        while(x != a[x]){
            x=a[x];
        }
        return x;
    }
    public boolean connected(int p, int q){
        return root(p)==root(q);
    }
    public void union(int p,int q, String timestamp){
        int i = root(p);
        int j = root(q);
        if(i == j) return;
        if(size[i] < size[j]){
            a[i] = j;
            size[j]+=size[i];
            if(size[j]==N){
                System.out.println("All Members are connected at Timestamp"+ timestamp);
            }
        }
        else{
            a[j] = i;
            size[i]+=size[j];
            if(size[i]==N){
                System.out.println("All Members are connected at Timestamp"+ timestamp);
            }
        }
    }

}
public class MyClass {
    public static void main(String args[]) {
      MyClas obj = new MyClas(6);
      obj.union(1,5, "2019-08-14 18:00:00");
      obj.union(2,4, "2019-08-14 18:00:01");
      obj.union(1,3, "2019-08-14 18:00:02");
      obj.union(5,2, "2019-08-14 18:00:03");
      obj.union(0,3,"2019-08-14 18:00:04");
      obj.union(2,1,"2019-08-14 18:00:05");

    }
}
"""
