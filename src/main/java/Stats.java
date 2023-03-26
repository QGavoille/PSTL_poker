import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Stats {


    public static void main(String[] args) throws IOException {
        for(int i = 0; i<52; i++){
            System.out.println(i);
            FileWriter fw = new FileWriter("/.test/"+i+".test");
            BufferedWriter bw = new BufferedWriter(fw);

            HashMap<Integer,Integer> posOcc = new HashMap<>();
            for(int k = 0; k<100000;k++){
                Partie p = new Partie();

                for(int tmp = 0; tmp<51;tmp++){
                    posOcc.put(tmp,0);
                }
                CardGame pack = p.getDeck();
                for(int k2 = 0; k2<52;k2++){
                    if(pack.getDeck()[k2].toInt()== i){
                        posOcc.replace(k2,posOcc.get(k2)+1);
                    }
                }

            }
            for(Integer k :posOcc.keySet() ){
                bw.write(""+k+"//"+posOcc.get(k));
            }
            bw.close();
        }




    }
}
