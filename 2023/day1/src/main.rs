use std::env;
use std::fs;
use std::ops::Deref;

use regex::Regex;


/// The input function can return any type that implements Clone
fn parse_input(file_path: &String) -> Vec<String>{
    dbg!(file_path);
    return std::fs::read_to_string(file_path).unwrap().lines().map(String::from).collect();
}

/// The part functions must take the input as an argument and return
/// anything implementing Display
fn part1(input: &[String]) {
    let mut sum = 0;
    for line in input{
        let mut first = -1;
        let mut last = 0;
        for ch in line.chars().enumerate(){
            let n = ch.1.to_string();
            if first == -1 && ch.1.is_numeric() {
                first = n.parse().unwrap();
                println!("{:?}", ch);
            }
            if ch.1.is_numeric() {
                last = n.parse().unwrap();
            }
        }
        println!("{}", first*10 + last);
        sum += first*10 + last;
    }
    dbg!(sum);
}


fn ugly_replace (line: String) -> String {
    let mut line_repl = line;
    line_repl = line_repl.replace("one", "o1one");
    line_repl = line_repl.replace("two", "t2two");
     line_repl = line_repl.replace("three", "t3three");
     line_repl = line_repl.replace("four", "f4four");
     line_repl = line_repl.replace("five", "f5five");
    line_repl = line_repl.replace("six", "s6six");
     line_repl = line_repl.replace("seven", "s7seven");
     line_repl = line_repl.replace("eight", "e8eight");
     line_repl = line_repl.replace("nine", "n9nine");
    return line_repl;
}

fn replacer(line: String) -> String {
    println!("{}", line);

    let re = Regex::new(r"(one|two|three|four|five|six|seven|eight|nine)").unwrap();
    let caps = re.find_iter(&line).map(|c| c);
    let mut first =  " ";
    let mut last = " ";
    for cap in caps {
        if first == " "  {
            first = cap.as_str();
        }
        last = cap.as_str();
    }
    dbg!(first);
    dbg!(last);

    let mut line_repl = line.clone();
    line_repl = ugly_replace(line_repl);
    // line_repl = replast(line_repl, last.to_string());
    // println!(line_repl);
    return line_repl;
}
fn part2(input: &[String]) {
    let mut sum = 0;
    for line in input{
        let mut line_repl: String = replacer(line.clone());

        println!("{}", line_repl);
        let mut first = -1;
        let mut last = 0;
        for ch in line_repl.chars().enumerate(){
            let n = ch.1.to_string();
            if first == -1 && ch.1.is_numeric() {
                first = n.parse().unwrap();
                println!("{:?}", ch);
            }
            if ch.1.is_numeric() {
                last = n.parse().unwrap();
            }
        }
        println!("{}", first*10 + last);
        sum += first*10 + last;
    }
    dbg!(sum);
}


fn main() {
    let args: Vec<String> = env::args().collect();

    let file_path = &args[1];
    let input = parse_input(file_path);
    dbg!(&input);

    // part1(&input);
    part2(&input);
}
