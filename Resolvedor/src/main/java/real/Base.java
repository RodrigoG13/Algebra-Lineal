package real;

import static java.lang.Math.sqrt;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Scanner;

/* @author Eidan Plata */
public class Base {

    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#.00");
        String tipo = "";
        String linea = "";
        String paseo;
        double dino, redondo;
        int i, j, variables, ecuaciones;
        i = 0;
        j = 0;
        ArrayList<ArrayList> vertical = new ArrayList<>();

        Scanner guarda = new Scanner(System.in);
        System.out.println("Ingrese el número de variables que tendrá el sistema");
        variables = guarda.nextInt();
        guarda.nextLine();
        System.out.println("Ingrese el número de ecuaciones que tendrá el sistema");
        ecuaciones = guarda.nextInt();
        guarda.nextLine();

        vertical = crear(vertical, variables, ecuaciones);

        vertical = llenar(vertical);

        imprimir(vertical);

        vertical = triangulo2(vertical);

        dino = clasificar(vertical, ecuaciones, variables);

        vertical = triangulo(vertical);

        imprimir(vertical);

        int limite;

        if (ecuaciones < variables) {
            limite = ecuaciones;
        } else {
            limite = variables;
        }

        int m = 0;
        int g = 0;
        while (m < vertical.size()) {
            paseo = vertical.get(m).get(vertical.get(0).size() - 1) + "";
            redondo = Double.parseDouble(paseo);
            if (redondo > 0 || redondo < 0) {

                g = g + 1;

            }
            m++;
        }

        int n = 0;
        int h = 0;
        int y = 0;
        int f = 0;
        while (n < vertical.size()) {
            while (y < vertical.get(0).size() - 2) {

                paseo = vertical.get(n).get(y) + "";
                redondo = Double.parseDouble(paseo);
                if (redondo > 0 || redondo < 0) {
                    h = h + 1;
                }
                y++;
            }
            if (h > 0 || h < 0) {
                f = f + 1;

            }
            y = 0;
            n++;
        }

        if (g > f || g < f) {
            dino = 3;
        }

        if (dino == 1) {
            while (i < limite) {
                linea = "";
                paseo = vertical.get(i).get(vertical.get(0).size() - 1) + "";
                redondo = Double.parseDouble(paseo);
                linea = linea + df.format(redondo) + "  ";
                System.out.println("X" + (i + 1) + " = " + linea);
                i++;
            }
            tipo = "EL SISTEMA TIENE UNA UNICA SOLUCION";
        } else {
            if (dino == 2) {

                while (i < limite) {
                    String signo;
                    int lama = limite;
                    linea = "";
                    paseo = vertical.get(i).get(vertical.get(0).size() - 1) + "";
                    redondo = Double.parseDouble(paseo);
                    linea = linea + df.format(redondo) + " ";
                    while (lama < variables) {
                        signo = "-";
                        paseo = vertical.get(i).get(lama) + "";
                        redondo = Double.parseDouble(paseo);
                        if (redondo <= 0) {
                            redondo = sqrt(redondo * redondo);
                            signo = "+";
                        }
                        linea = linea + signo + " " + df.format(redondo) + "p" + (lama - limite + 1) + " ";
                        lama++;
                    }
                    System.out.println("X" + (i + 1) + " = " + linea);
                    i++;
                }
                int lama = limite;
                while (lama < variables) {
                    System.out.println("X" + ((lama) + 1) + " = p" + (lama - limite + 1));
                    lama++;
                }

                tipo = "EL SISTEMA TIENE UNA INFINIDAD DE SOLUCIONES";
            } else {
                tipo = "EL SISTEMA NO TIENE SOLUCION";
            }
        }

        System.out.println("CASO: " + dino + " " + tipo);
    }

    public static ArrayList<ArrayList> crear(ArrayList<ArrayList> vertical, int variables, int ecuaciones) {
        int i, j;
        i = 0;
        j = 0;
        while (i < ecuaciones) {
            ArrayList horizontal = new ArrayList<Double>();
            while (j < variables + 1) {
                horizontal.add(0);
                j++;
            }
            j = 0;
            vertical.add(horizontal);
            i++;
        }
        return vertical;
    }

    public static void imprimir(ArrayList<ArrayList> vertical) {
        DecimalFormat df = new DecimalFormat("#.00");
        String paseo;
        int i, j, k, variables, ecuaciones;
        double redondo;
        i = 0;
        j = 0;
        ecuaciones = vertical.size();
        variables = vertical.get(0).size();

        while (i < ecuaciones) {
            String linea = "";
            while (j < variables) {
                paseo = vertical.get(i).get(j) + "";
                redondo = Double.parseDouble(paseo);
                linea = linea + df.format(redondo) + "  ";
                j++;
            }
            j = 0;

            System.out.println(linea);
            i++;
        }
        System.out.println("----------------------------");

    }

    public static ArrayList<ArrayList> llenar(ArrayList<ArrayList> vertical) {
        Scanner guarda = new Scanner(System.in);
        int i, j;
        i = 0;
        j = 0;
        while (i < vertical.size()) {
            System.out.println("Ingrese la ecuacion " + (i + 1) + " en la forma ax1+bx2+cx3=d sin espacios");
            String ecu = guarda.next();
            guarda.nextLine();
            ecu = ecu.trim();
            char x = 'x';
            char z = '=';
            int k = 0;
            while (j < ecu.length()) {
                String coe = "";
                char y = ecu.charAt(j);
                if (y == x) {
                    if (j == k) {
                        int n = Integer.parseInt(ecu.charAt(j + 1) + "") - 1;
                        vertical.get(i).set(n, 1);
                    } else {
                        if ((j - k) == 1 && j > 1) {
                            coe = ecu.charAt(k) + "1";
                            coe = coe.trim();
                            int n = Integer.parseInt(ecu.charAt(j + 1) + "") - 1;
                            double rcoe = Double.parseDouble(coe);
                            vertical.get(i).set(n, rcoe);
                        } else {
                            if (j == 1) {
                                char menos = '-';
                                if (ecu.charAt(k) == menos) {
                                    coe = coe + "-1";
                                    k++;
                                }
                            }
                            while (k < j) {
                                coe = coe + ecu.charAt(k);
                                k++;
                            }
                            coe = coe.trim();
                            int n = Integer.parseInt(ecu.charAt(j + 1) + "") - 1;
                            double rcoe = Double.parseDouble(coe);
                            vertical.get(i).set(n, rcoe);
                        }
                    }
                    k = j + 2;
                } else {
                    if (y == z) {
                        k = j + 1;
                        while (k < ecu.length()) {
                            coe = coe + ecu.charAt(k);
                            k++;
                        }
                        coe = coe.trim();
                        int n = (vertical.get(i).size() - 1);
                        double rcoe = Double.parseDouble(coe);
                        vertical.get(i).set(n, rcoe);
                    }
                }
                j++;
            }
            i++;
            j = 0;
        }
        System.out.println("----------------------------");
        return vertical;
    }

    public static ArrayList<ArrayList> diagonal(ArrayList<ArrayList> vertical, int pospivote) {
        int numCo;
        int numEc;
        String paseo;
        double pivote;
        double paseo2, paseo3, paseo4;
        numCo = vertical.get(0).size();
        numEc = vertical.size();
        int limite;

        if (numEc < numCo - 1) {
            limite = numEc;
        } else {
            limite = numCo - 1;
        }

        if (pospivote < limite - 1) {

            int i, j;
            paseo = vertical.get(pospivote).get(pospivote) + "";
            pivote = Double.parseDouble(paseo);

            i = pospivote + 1;
            j = pospivote;

            paseo = vertical.get(i).get(pospivote) + "";
            paseo2 = Double.parseDouble(paseo);
            if (paseo2 == 0.0 || paseo2 == -0.0 || paseo2 == 0) {
                System.out.println("EntrÃ©");
                vertical = ordenar1(vertical, pospivote);
                System.out.println("Ya quedÃ³");
            } else {
                System.out.println("No es un cero la posicion " + pospivote);
            }

            while (i < limite) {
                while (j < numCo) {
                    paseo = vertical.get(pospivote).get(j) + "";
                    paseo2 = Double.parseDouble(paseo);
                    vertical.get(pospivote).set(j, paseo2 / pivote);
                    j++;
                }
                j = pospivote;
                paseo = vertical.get(i).get(pospivote) + "";
                paseo2 = Double.parseDouble(paseo);
                while (j < numCo) {

                    paseo = vertical.get(pospivote).get(j) + "";
                    paseo3 = Double.parseDouble(paseo);
                    paseo = vertical.get(i).get(j) + "";
                    paseo4 = Double.parseDouble(paseo);

                    vertical.get(i).set(j, (paseo2 * paseo3) - paseo4);
                    j++;
                }
                i++;
            }

            vertical = diagonal(vertical, pospivote + 1);
            imprimir(vertical);
        }
        return vertical;
    }

    public static ArrayList<ArrayList> triangulo2(ArrayList<ArrayList> vertical) {
        int i, j, k, numEc, numCo;
        i = 0;
        String paseo;
        double pivote;
        double fpivote, fnocero, multiplicador;
        numCo = vertical.get(0).size();
        numEc = vertical.size();
        int limite;

        if (numEc < numCo - 1) {
            limite = numEc;
        } else {
            limite = numCo - 1;
        }

        //System.out.println();
        while (i < limite) {

            k = i + 1;
            j = 0;
            double paseo2;
            paseo = vertical.get(i).get(i) + "";
            paseo2 = Double.parseDouble(paseo);
            if (paseo2 == 0.0 || paseo2 == -0.0 || paseo2 == 0) {

                vertical = ordenar1(vertical, i);

            } else {

            }
            paseo = vertical.get(i).get(i) + "";
            pivote = Double.parseDouble(paseo);
            while (j < numCo) {
                paseo = vertical.get(i).get(j) + "";
                fpivote = Double.parseDouble(paseo);
                vertical.get(i).set(j, fpivote / pivote);
                j++;
            }

            while (k - i < (numEc - i)) {
                j = 0;
                paseo = vertical.get(k).get(i) + "";
                multiplicador = Double.parseDouble(paseo);
                while (j < numCo) {
                    paseo = vertical.get(i).get(j) + "";
                    fpivote = Double.parseDouble(paseo);
                    paseo = vertical.get(k).get(j) + "";
                    fnocero = Double.parseDouble(paseo);
                    vertical.get(k).set(j, ((multiplicador * fpivote) - fnocero));
                    j++;
                    //System.out.println("----------------------------");
                    //System.out.println(j);
                }

                //System.out.println("----------------------------");
                //System.out.println(k);
                k++;
            }
            //System.out.println("----------------------------");
            //System.out.println(i);
            imprimir(vertical);
            i++;
        }

        paseo = vertical.get(0).get(0) + "";
        pivote = Double.parseDouble(paseo);
        j = 0;
        while (j < numCo) {
            paseo = vertical.get(0).get(j) + "";
            fpivote = Double.parseDouble(paseo);
            vertical.get(0).set(j, fpivote / pivote);
            j++;
        }

        return vertical;
    }

    public static ArrayList<ArrayList> triangulo3(ArrayList<ArrayList> vertical, int acabo) {
        int i, j, k, numEc, numCo;
        i = 1;
        String paseo;
        double pivote;
        double fpivote, fnocero, multiplicador;
        numCo = vertical.get(0).size();
        numEc = vertical.size();
        int limite = acabo;

        //System.out.println();
        while (i < limite) {

            k = 1;
            j = 0;
            paseo = vertical.get(limite - i).get(limite - i) + "";

            pivote = Double.parseDouble(paseo);

            while (j < numCo) {
                paseo = vertical.get(limite - i).get(j) + "";
                fpivote = Double.parseDouble(paseo);
                vertical.get(limite - i).set(j, fpivote / pivote);
                j++;
            }

            while (k < (limite - (i - 1))) {
                j = 0;
                paseo = vertical.get(limite - i - (k)).get(limite - i) + "";
                multiplicador = Double.parseDouble(paseo);
                while (j < numCo) {
                    paseo = vertical.get(limite - i).get(j) + "";
                    fpivote = Double.parseDouble(paseo);
                    paseo = vertical.get(limite - i - (k)).get(j) + "";
                    fnocero = Double.parseDouble(paseo);
                    vertical.get(limite - i - (k)).set(j, ((multiplicador * fpivote) - fnocero));
                    j++;
                    //System.out.println("----------------------------");
                    //System.out.println(j);
                }

                //System.out.println("----------------------------");
                //System.out.println(k);
                k++;
            }
            //System.out.println("----------------------------");
            //System.out.println(i);
            imprimir(vertical);
            i++;
        }

        paseo = vertical.get(0).get(0) + "";
        pivote = Double.parseDouble(paseo);
        j = 0;
        while (j < numCo) {
            paseo = vertical.get(0).get(j) + "";
            fpivote = Double.parseDouble(paseo);
            vertical.get(0).set(j, fpivote / pivote);
            j++;
        }

        return vertical;
    }

    public static ArrayList<ArrayList> triangulo(ArrayList<ArrayList> vertical) {
        int i, j, k, numEc, numCo;
        i = 1;
        String paseo;
        double pivote;
        double fpivote, fnocero, multiplicador;
        numCo = vertical.get(0).size();
        numEc = vertical.size();
        int limite;

        if (numEc < numCo - 1) {
            limite = numEc;
        } else {
            limite = numCo - 1;
        }

        //System.out.println();
        while (i < limite) {
            k = 1;
            j = 0;
            paseo = vertical.get(limite - i).get(limite - i) + "";
            pivote = Double.parseDouble(paseo);
            while (j < numCo) {
                paseo = vertical.get(limite - i).get(j) + "";
                fpivote = Double.parseDouble(paseo);
                vertical.get(limite - i).set(j, fpivote / pivote);
                j++;
            }

            while (k < (limite - (i - 1))) {
                j = 0;
                paseo = vertical.get(limite - i - (k)).get(limite - i) + "";
                multiplicador = Double.parseDouble(paseo);
                while (j < numCo) {
                    paseo = vertical.get(limite - i).get(j) + "";
                    fpivote = Double.parseDouble(paseo);
                    paseo = vertical.get(limite - i - (k)).get(j) + "";
                    fnocero = Double.parseDouble(paseo);
                    vertical.get(limite - i - (k)).set(j, ((multiplicador * fpivote) - fnocero));
                    j++;
                    //System.out.println("----------------------------");
                    //System.out.println(j);
                }

                //System.out.println("----------------------------");
                //System.out.println(k);
                k++;
            }
            //System.out.println("----------------------------");
            //System.out.println(i);
            imprimir(vertical);
            i++;
        }

        paseo = vertical.get(0).get(0) + "";
        pivote = Double.parseDouble(paseo);
        j = 0;
        while (j < numCo) {
            paseo = vertical.get(0).get(j) + "";
            fpivote = Double.parseDouble(paseo);
            vertical.get(0).set(j, fpivote / pivote);
            j++;
        }

        return vertical;
    }

    public static ArrayList<ArrayList> ordenar1(ArrayList<ArrayList> vertical, int cero) {
        ArrayList<ArrayList> clon = new ArrayList<>();
        clon = vertical;
        String paseo;
        int i, j, k, l;
        double intento, fpivote;
        i = cero;
        k = i + 1;
        l = 0;

        while (k < vertical.size()) {
            paseo = vertical.get(k).get(i) + "";
            intento = Double.parseDouble(paseo);
            if (intento == 0.0 || intento == -0.0 || intento == 0) {
                k++;
            } else {
                j = 0;
                while (j < vertical.get(0).size()) {
                    paseo = vertical.get(k).get(j) + "";
                    fpivote = Double.parseDouble(paseo);
                    clon.get(i).set(j, fpivote);
                    j++;
                }
                j = 0;
                while (j < vertical.get(0).size()) {
                    paseo = vertical.get(i).get(j) + "";
                    fpivote = Double.parseDouble(paseo);
                    clon.get(k).set(j, fpivote);
                    j++;
                }
                l = 1;
                break;
            }

        }

        if (l == 0) {
            clon = ordenar2(vertical, cero);
        }

        return clon;
    }

    public static ArrayList<ArrayList> ordenar2(ArrayList<ArrayList> vertical, int cero) {
        ArrayList<ArrayList> clon = new ArrayList<>();
        ArrayList<ArrayList> clon2 = new ArrayList<>();
        clon = vertical;
        clon2 = vertical;
        String paseo;
        int i, j, k, l;
        double intento, fpivote, kpivote;
        i = 0;
        j = cero;
        k = j + 1;
        l = 0;

        while (k < (vertical.get(0).size())) {
            paseo = vertical.get(cero).get(k) + "";
            intento = Double.parseDouble(paseo);
            if (intento > 0 || intento < 0) {
                while (i < vertical.size()) {
                    paseo = vertical.get(i).get(k) + "";
                    fpivote = Double.parseDouble(paseo);
                    clon.get(i).set(cero, fpivote);
                    i++;
                }
                i = 0;

                clon = ordenar3(clon, clon2, k, cero);

                l = 1;
                break;
            }
            k++;
        }

        if (l == 0) {
            DecimalFormat df = new DecimalFormat("#.00");
            int acabo = cero;
            int limite = acabo;
            String linea;
            double redondo;
            vertical = triangulo3(vertical, acabo);
            int variables = vertical.get(0).size() - 1;
            int dino = 0;

            int m = 0;
            int g = 0;
            while (m < vertical.size()) {
                paseo = vertical.get(m).get(vertical.get(0).size() - 1) + "";
                redondo = Double.parseDouble(paseo);
                if (redondo > 0 || redondo < 0) {

                    g = g + 1;
                }
                m++;
            }

            int n = 0;
            int h = 0;
            int y = 0;
            int f = 0;
            while (n < vertical.size()) {
                while (y < vertical.get(0).size() - 2) {
                    paseo = vertical.get(n).get(y) + "";
                    redondo = Double.parseDouble(paseo);
                    if (redondo > 0 || redondo < 0) {
                        h = h + 1;
                    }
                    y++;
                }
                if (h > 0 || h < 0) {
                    f = f + 1;
                }
                y = 0;
                n++;
            }

            if (h == f) {
                dino = 2;
            } else {
                dino = 3;
            }

            System.out.println(h);
            System.out.println("sospechoso = " + f);

            if (dino == 3) {

                System.out.println("CASO 3: EL SISTEMA NO TIENE SOLUCION");
                System.exit(0);

            } else {

                while (i < limite) {
                    String signo;
                    int lama = limite;
                    linea = "";
                    paseo = vertical.get(i).get(vertical.get(0).size() - 1) + "";
                    redondo = Double.parseDouble(paseo);
                    linea = linea + df.format(redondo) + " ";
                    while (lama < variables) {
                        signo = "-";
                        paseo = vertical.get(i).get(lama) + "";
                        redondo = Double.parseDouble(paseo);
                        if (redondo <= 0) {
                            redondo = sqrt(redondo * redondo);
                            signo = "+";
                        }
                        linea = linea + signo + " " + df.format(redondo) + "p" + (lama - limite + 1) + " ";
                        lama++;
                    }
                    System.out.println("X" + (i + 1) + " = " + linea);
                    i++;
                }
                int lama = limite;
                while (lama < variables) {
                    System.out.println("X" + ((lama) + 1) + " = p" + (lama - limite + 1));
                    lama++;
                }

                System.out.println("CASO 2: EL SISTEMA TIENE UNA INFINIDAD DE SOLUCIONES");
                System.exit(0);

            }

        }
        return clon;
    }

    public static ArrayList<ArrayList> ordenar3(ArrayList<ArrayList> clon, ArrayList<ArrayList> vertical, int k, int cero) {
        String paseo;
        int i, j, l;
        double intento, fpivote, kpivote;
        i = 0;
        j = cero;
        l = 0;

        while (i < (vertical.size())) {

            paseo = vertical.get(i).get(j) + "";
            fpivote = Double.parseDouble(paseo);
            clon.get(i).set(k, fpivote);
            i++;
        }

        return clon;
    }

    public static int clasificar(ArrayList<ArrayList> vertical, int ecuaciones, int variables) {
        int res = 0;
        String paseo;
        double paseo2;
        int numCA = 0;
        int numCC = 0;
        int i = 0;
        int j = 0;

        while (i < vertical.size()) {
            while (j < vertical.get(0).size()) {
                paseo = vertical.get(i).get(i) + "";
                paseo2 = Double.parseDouble(paseo);
                if (paseo2 == 0.0 || paseo2 == -0.0 || paseo2 == 0) {
                    numCA++;
                }
                j++;
            }
            i++;
        }

        while (i < vertical.size() - 1) {
            while (j < vertical.get(0).size()) {
                paseo = vertical.get(i).get(j) + "";
                paseo2 = Double.parseDouble(paseo);
                if (paseo2 == 0.0 || paseo2 == -0.0 || paseo2 == 0) {
                    numCC++;
                }
                j++;
            }
            i++;
        }

        if (numCA == numCC) {
            if (ecuaciones < variables) {
                res = 2;
            } else {
                res = 1;
            }
        } else {

            res = 3;
        }

        return res;
    }
}
