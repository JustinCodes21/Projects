
import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;
import java.util.Vector;


public class NFA2DFA 
{
    public static void main(String[] args) throws Exception 
    {
        NFAConvert nfa2dfa = new NFAConvert();
        nfa2dfa.parseNFA(args[0]);
    }

    public static int startingQ =0;
    public static int endingQ =0;

    static class NFAConvert 
    {

        // 5-tuple list formal definition of finite automata - (Q, Sigma, delta
        // function, initial state, final state)

        private int Q = -1;
        List<Character> sigma = new ArrayList<>();
        private Map<Integer, Map<Character, Set<Integer>>> deltaFunction = new HashMap<>();
        private int initialState = -1;
        private List<Integer> acceptingStates = new ArrayList<>();
        private List<String> input = new ArrayList<>();

        void parseNFA(String inputFile) throws FileNotFoundException 
        {

            File myObj = new File(inputFile);
            Scanner myReader = new Scanner(myObj);

            // begin reading
            String data = myReader.nextLine();

            // get number of states
            data = data.replaceAll("[^0-9]", " ");
            data = data.replaceAll(" +", "");
            Q = Integer.parseInt(String.valueOf(data));
            data = myReader.nextLine();
            data = data.replaceAll("Sigma: ", " ");
            data = data.replaceAll(" ", "");
            for (char ch : data.toCharArray()) {
                sigma.add(ch);
            }

            sigma.add('\u03B5'); // ASCII code for epsilon/lambda

            data = myReader.nextLine();// burn the dashed line

            // get state details
            for (int i = 0; i < Q; i++) 
            {
                data = myReader.nextLine();

                String[] pieces = data.split(":");
                Map<Character, Set<Integer>> transitions = new HashMap<>();

                if (pieces.length == 2) 
                {
                    String statePieces = pieces[1].trim();
                    String[] statePiecesNoSpaces = statePieces.split(" ");

                    for (int j = 0; j < sigma.size(); j++) 
                    {
                        String transitionsWithNoBraces = statePiecesNoSpaces[j].replaceAll("[{}]", ""); // no braces and no
                                                                                                        // commas
                        String[] destinationStates = transitionsWithNoBraces.trim().split(",");

                        Set<Integer> destStates = new HashSet<>();

                        for (String state : destinationStates) 
                        {
                            if (state.equals("")) 
                            {
                                continue;
                            }
                            destStates.add(Integer.parseInt(state)); // just want the integers
                        }

                        transitions.put(sigma.get(j), destStates); // key: letter, value: Destination states
                    }
                }

                deltaFunction.put(i, transitions);
            }
            

            // get inital state
            data = myReader.nextLine();// dashed line

            data = myReader.nextLine();

            String[] initialStateParts = data.split(":");
            if (initialStateParts.length == 2) {
                String state = initialStateParts[1].trim();
                initialState = Integer.parseInt(state);
            }

            // get accepting state
            data = myReader.nextLine();

            int colon = data.indexOf(":");
            colon += 2;// next index after colon space

            String state = data.substring(colon);
            String[] states = state.split(",");

            for (String token : states) {
                acceptingStates.add(Integer.parseInt(token));
            }

            // get input strings
            data = myReader.nextLine(); // discard empty line
            data = myReader.nextLine();

            while (myReader.hasNextLine()) {
                data = myReader.nextLine();
                input.add(data); // Add each alphabet input line into list
                
            }

            myReader.close();

            convertToDFA(inputFile, Q, sigma, deltaFunction, initialState, acceptingStates, input); // NFA -> DFA
        }


    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //////////NFA to DFA Start//////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
    public static void convertToDFA(String inputFile, int Q, List<Character> sigma,
            Map<Integer, Map<Character, Set<Integer>>> deltaFunction, int initialState, List<Integer> acceptingStates, List<String> input) 
    {
        Vector<State> dfaStates = new Vector<>();
        Queue<State> unprocessedStates = new LinkedList<>();

        // Create the initial state of the DFA
        Set<Integer> initialDFAStateSet = lamdaClosure(Set.of(initialState), deltaFunction);
        State initialDFAState = new State(dfaStates.size(), initialDFAStateSet);
        
        //Check for accepting
        Integer[] tempSet = new Integer[initialDFAState.set.size()];
        initialDFAState.set.toArray(tempSet);
        for(int x = 0; x < tempSet.length; x++)
        {
            if(acceptingStates.contains(tempSet[x]))
            {
                initialDFAState.accepting=true;
            }
        }

        dfaStates.add(initialDFAState);
        unprocessedStates.add(initialDFAState);

        while (!unprocessedStates.isEmpty()) 
        {
            State currentDFAState = unprocessedStates.poll();

            for (char symbol : sigma) 
            {
                Set<Integer> nextStateSet = lamdaClosure(move(currentDFAState.set, symbol, deltaFunction), deltaFunction);
                
                if (!nextStateSet.isEmpty()) 
                {
                    State nextState = new State(dfaStates.size(), nextStateSet);
                    
                    if (!dfaStates.contains(nextState)) 
                    {
                        //Check for accepting
                        tempSet = new Integer[nextState.set.size()];
                        nextState.set.toArray(tempSet);
                        for(int x = 0; x < tempSet.length; x++)
                        {
                            if(acceptingStates.contains(tempSet[x]))
                            {
                                nextState.accepting=true;
                            }
                        }
                        dfaStates.add(nextState);
                        unprocessedStates.add(nextState);
                        currentDFAState.paths.add(nextState.id);
                    }
                    else 
                    {
                        State existingState = dfaStates.get(dfaStates.indexOf(nextState));

                        // Add a path to the existing state in dfaStates
                        currentDFAState.paths.add(existingState.id);
                    }
                }
                else
                { //if the new set is empty, that means trap state.
                    currentDFAState.paths.add(-1);
                }
            }
        }
        startingQ = dfaStates.size();
        System.out.println("\nNFA " + inputFile + " to DFA:\n");
        printDFA(inputFile, sigma, dfaStates);
        DFASolve(dfaStates, sigma, input, inputFile);
        minimizedDFA(dfaStates, sigma, input, inputFile);

    }

        private static Set<Integer> lamdaClosure(Set<Integer> states, Map<Integer, Map<Character, Set<Integer>>> deltaFunction) 
        {
            Set<Integer> closure = new HashSet<>(states);
            Stack<Integer> stack = new Stack<>();
            stack.addAll(states);

            while (!stack.isEmpty()) 
            {
                int currentState = stack.pop();

                if (deltaFunction.containsKey(currentState) && deltaFunction.get(currentState).containsKey('\u03B5')) 
                {
                    for (int nextState : deltaFunction.get(currentState).get('\u03B5')) 
                    {
                        if (closure.add(nextState)) 
                        {
                            stack.push(nextState);
                        }
                    }
                }
            }
            return closure;
        }

        private static Set<Integer> move(Set<Integer> states, char sigma, Map<Integer, Map<Character, Set<Integer>>> deltaFunction) 
        {
            Set<Integer> result = new HashSet<>();

            for (int state : states) 
            {
                if (deltaFunction.containsKey(state) && deltaFunction.get(state).containsKey(sigma)) 
                {
                    result.addAll(deltaFunction.get(state).get(sigma));
                }
            }
            return result;
        }

        private static void printDFA(String inputFile, List<Character> sigma, Vector<State> dfaStates) 
        {
            System.out.print("Sigma:\t");
            for(int i = 0; i < sigma.size() - 1; i++)
            {
                System.out.print(sigma.get(i) + "\t");
                
            }
            System.out.println("");
            for(int i = 0; i < sigma.size() - 1; i++)
            {
                System.out.print("---------");
                
            }
            System.out.println("");

            for(int x = 0; x < dfaStates.size(); x++)
            {
                System.out.print(" " + dfaStates.elementAt(x).id + ":\t");
                for(int y = 0; y < dfaStates.elementAt(x).paths.size() -1; y++)
                {
                    System.out.print( dfaStates.elementAt(x).paths.get(y)+ "\t");
                }
                System.out.println("");
            }

            for(int i = 0; i < sigma.size() - 1; i++)
            {
                System.out.print("---------");

            }
            System.out.println("");     

            System.out.println("0: Initial State");
            for(int x = 0; x < dfaStates.size(); x++)
            {
                if(dfaStates.elementAt(x).accepting == true)
                {
                    System.out.print(dfaStates.elementAt(x).id + ",");
                }
            }
            System.out.println(": Accepting State(s)");
        }

        static class State {
        public int id;
        public Vector<Integer> paths = new Vector<>();
        public Set<Integer> set = new HashSet<>();
        public boolean accepting = false;

        public State(int id, Set<Integer> set) {
            this.id = id;
            this.set = set;
        }

        // Override equals and hashCode to properly compare State objects
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            State state = (State) o;
            return id == state.id ||
                    set.equals(state.set);
        }
    }
    
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //////////NFA to DFA End//////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////   

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //////////DFA Minimization Start//////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
        public static void minimizedDFA(Vector<State> dfaStates, List<Character> sigma, List<String>input, String inputFile)
        {
    
            boolean areWeDone = true;
            boolean haveMatch = false;

            do{
                areWeDone = true;
                haveMatch = false;
                //for each state
                for(int currState = 0; currState < dfaStates.size(); currState++)
                {   //compare to states that follow it
                    for(int matchState = currState+1; matchState < dfaStates.size(); matchState++)
                    {
                        if(pathEqual(dfaStates.get(currState), dfaStates.get(matchState)) && haveMatch == false)
                        {
                            haveMatch = true;
                            areWeDone = false;
                            //if equal, merge states and redirect all paths.

                            //remove the redundant state
                            dfaStates.remove(matchState);
                            //redirect all paths
                            for(int exchangeState = 0; exchangeState < dfaStates.size(); exchangeState++)
                            {
                                for(int letter = 0; letter < sigma.size()-1; letter++)
                                {
                                    if(dfaStates.get(exchangeState).paths.get(letter).intValue() == matchState)
                                    {
                                        dfaStates.get(exchangeState).paths.set(letter, currState);
                                    }
                                }
                            }
                        }
                    }
                }
            }while(areWeDone == false);
            endingQ = dfaStates.size();
            System.out.println("Minimized DFA:\n\n");
            printDFA(inputFile, sigma, dfaStates);

            DFASolve(dfaStates, sigma, input, inputFile);
            System.out.println("|Q| " + startingQ + " -> " + endingQ);
        }


        private static boolean pathEqual(State currState, State matchState)
        {
            for(int currSigma = 0; currSigma < currState.paths.size()-1; currSigma++)
            {
                if(!currState.paths.get(currSigma).equals(matchState.paths.get(currSigma)))
                {
                    return false;
                }
            }
            return true;
        }

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //////////DFA Minimization End//////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////            
        static void DFASolve(Vector<State> states, List<Character> sigma, List<String> input, String inputFile)
        {   
            System.out.println("\nParsing results of strings attached in " + inputFile + ":");
            boolean trapState = false;
            int lineCount = 0;
            int yesCounter = 0;
            int noCounter = 0;
            //for each input line
            for(int line = 0; line < input.size(); line++)
            {
                State currState = states.get(0);
                
                //use the next letter to get to the next state.
                char[] inputCharArray = input.get(line).toCharArray();
                for(int letter = 0; letter < inputCharArray.length; letter++)
                {
                    int inputSigma = sigma.indexOf(inputCharArray[letter]);
                    if(currState.paths.size() > inputSigma)
                    {
                        if( currState.paths.get(inputSigma) == -1 )
                        {
                            trapState = true;
                            break;
                        }
                        else
                        {
                            for(int x = 0; x < states.size(); x++)
                            {
                                if(states.get(x).id == currState.paths.get(inputSigma))
                                {
                                    currState = states.get(x);
                                }
                            }
                        }
                    }

                }// end of line
                
                if(currState.accepting == true && trapState == false)
                {
                    System.out.print("Yes ");
                    yesCounter+=1;
                }
                else
                {
                    System.out.print("No ");
                    noCounter+=1;
                }
                trapState = false;
                lineCount++;
                //move to a new line when we're halfway through the input strings.
                if(lineCount == 15)
                {
                    System.out.println("");
                }
            }
            
            System.out.println("\n\nYes: " + yesCounter + " No: " + noCounter);
            System.out.println("");

        }

    }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////End of File///////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////


