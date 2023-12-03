use regex::Regex;
use core::num;
use std::env;
use std::fs;
use std::ops::Deref;
use std::collections::HashSet;
use std::collections::HashMap;


fn parse_input(file_path: &String) -> Vec<String> {
    dbg!(file_path);
    return std::fs::read_to_string(file_path)
        .unwrap()
        .lines()
        .map(String::from)
        .collect();
}

fn is_valid(char_set:HashSet::<(i32, i32)>, num_pos:(i32, i32) ) -> bool{
    let (row, col) = num_pos; 
    if char_set.contains(&(row - 1, col)) {
        return true;
    }
    if char_set.contains(&(row + 1, col)) {
        return true;
    }
    if char_set.contains(&(row, col - 1)) {
        return true;
    }
    if char_set.contains(&(row, col + 1)) {
        return true;
    }
    if char_set.contains(&(row - 1, col - 1)) {
        return true;
    }
    if char_set.contains(&(row - 1, col + 1)) {
        return true;
    }
    if char_set.contains(&(row + 1, col - 1)) {
        return true;
    }
    if char_set.contains(&(row + 1, col + 1)) {
        return true;
    }

    
    return false;
}
fn part1(input: &[String]) {
    let mut char_set = HashSet::<(i32, i32)>::new();
    let mut line_num = 0;
    for line in input {
        for (col, ch) in line.chars().enumerate() {
            if !ch.is_numeric() && ch != '.' {
                char_set.insert((line_num, col as i32));
                println!("{}", col);
            }
        }
        line_num += 1;
    }

    let re_numbers = Regex::new(r"([0-9]+)").unwrap();

    let mut sum = 0;
    let mut index = 0;
    let mut row: i32 = 0;
    for line in input {
        let caps = re_numbers.captures_iter(&line).map(|c| c);
        for cap in caps {
            let num: i32 = cap.get(0).unwrap().as_str().parse().unwrap();
            // println!("Hej: {}", num);
            let start: i32 = cap.get(0).unwrap().start() as i32;
            let end: i32 = cap.get(0).unwrap().end() as i32;
            let mut valid = false;
            for col in start..end {
                if is_valid(char_set.clone(), (row, col)) {
                    valid = true;
                }
            }
            if valid {
                sum += num;

            }
        }
        row += 1;
        // println!("{}", red_caps);

    }
    dbg!(sum);
}

fn is_valid2(char_set:HashSet::<(i32, i32)>, num_pos:(i32, i32) ) -> (i32, i32){
    let (row, col) = num_pos; 
    if char_set.contains(&(row - 1, col)) {
        return (row - 1, col);
    }
    if char_set.contains(&(row + 1, col)) {
        return (row + 1, col);
    }
    if char_set.contains(&(row, col - 1)) {
        return (row, col - 1);
    }
    if char_set.contains(&(row, col + 1)) {
        return (row, col + 1);
    }
    if char_set.contains(&(row - 1, col - 1)) {
        return (row - 1, col - 1);
    }
    if char_set.contains(&(row - 1, col + 1)) {
        return (row - 1, col + 1);
    }
    if char_set.contains(&(row + 1, col - 1)) {
        return (row + 1, col - 1);
    }
    if char_set.contains(&(row + 1, col + 1)) {
        return (row + 1, col + 1);
    }

    
    return (-1, -1);
}

fn part2(input: &[String]) {
    let mut char_set = HashSet::<(i32, i32)>::new();
    let mut line_num = 0;
    let mut neigh = HashMap::<(i32, i32),  Vec<i32>>::new();

    for line in input {
        for (col, ch) in line.chars().enumerate() {
            if ch == '*' {
                char_set.insert((line_num, col as i32));
                println!("{}", col);
                neigh.insert((line_num, col as i32), Vec::<i32>::new());

            }
        }
        line_num += 1;
    }
    dbg!(char_set.clone());

    let re_numbers = Regex::new(r"([0-9]+)").unwrap();
    let mut sum = 0;
    let mut index = 0;
    let mut row: i32 = 0;
    for line in input {
        let caps = re_numbers.captures_iter(&line).map(|c| c);
        for cap in caps {
            // dbg!(cap);
            let num: i32 = cap.get(0).unwrap().as_str().parse().unwrap();
            println!("Hej: {}", num);
            let start: i32 = cap.get(0).unwrap().start() as i32;
            let end: i32 = cap.get(0).unwrap().end() as i32;
            let mut valid = false;
            for col in start..end {
                let mut g_row = -1;
                let mut g_col = -1;
                (g_row, g_col) = is_valid2(char_set.clone(), (row, col));
                if (g_row, g_col) != (-1, -1) {
                    let mut vec = neigh.get(&(g_row, g_col)).unwrap().clone();
                    vec.push(num);
                    neigh.insert((g_row, g_col), vec);
                    break;
                }

            }
        }
        row += 1;
        // println!("{}", red_caps);

    }
    for (k, v) in neigh {
        if v.len() > 1 {
            let mut prod = 1;
            for val in v{
                prod *= val;
            }
            sum += prod;
        }
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
