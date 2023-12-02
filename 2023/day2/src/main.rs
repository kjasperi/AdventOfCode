use regex::Regex;
use std::env;
use std::fs;
use std::ops::Deref;

fn parse_input(file_path: &String) -> Vec<String> {
    dbg!(file_path);
    return std::fs::read_to_string(file_path)
        .unwrap()
        .lines()
        .map(String::from)
        .collect();
}

fn part1(input: &[String]) {
    let total_red = 12;
    let total_green = 13;
    let total_blue = 14;

    let re_red = Regex::new(r"([0-9]+) red").unwrap();
    let re_green = Regex::new(r"([0-9]+) green").unwrap();
    let re_blue = Regex::new(r"([0-9]+) blue").unwrap();

    let mut sum = 0;
    let mut index = 1;
    for line in input {
        let mut possible = true;

        let red_caps = re_red.captures_iter(&line).map(|c| c);
        for red_cap in red_caps {
            let num: i32 = red_cap.get(1).unwrap().as_str().parse().unwrap();
            println!("Hej: {}", num);
            if num > total_red {
                possible = false;
            }
        }
        let green_caps = re_green.captures_iter(&line).map(|c| c);
        for green_cap in green_caps {
            let num: i32 = green_cap.get(1).unwrap().as_str().parse().unwrap();
            println!("Hej: {}", num);
            if num > total_green {
                possible = false;
            }
        }
        let blue_caps = re_blue.captures_iter(&line).map(|c| c);
        for blue_cap in blue_caps {
            let num: i32 = blue_cap.get(1).unwrap().as_str().parse().unwrap();
            println!("Hej: {}", num);
            if num > total_blue {
                possible = false;
            }
        }
        if possible {
            println!("{}", line);
            sum += index;
        }
        index += 1;

    }
    dbg!(sum);
}

fn part2(input: &[String]) {
    let re_red = Regex::new(r"([0-9]+) red").unwrap();
    let re_green = Regex::new(r"([0-9]+) green").unwrap();
    let re_blue = Regex::new(r"([0-9]+) blue").unwrap();

    let mut sum = 0;
    let mut index = 1;
    for line in input {
        let mut possible = true;
        let mut max_red = 0;
        let red_caps = re_red.captures_iter(&line).map(|c| c);
        for red_cap in red_caps {
            let num: i32 = red_cap.get(1).unwrap().as_str().parse().unwrap();
            if num > max_red {
                max_red = num;
            }
        }
        dbg!(max_red);
        let green_caps = re_green.captures_iter(&line).map(|c| c);
        let mut max_green = 0;
        for green_cap in green_caps {
            let num: i32 = green_cap.get(1).unwrap().as_str().parse().unwrap();
            if num > max_green {
                max_green = num;
            }
        }
        let blue_caps = re_blue.captures_iter(&line).map(|c| c);
        let mut max_blue = 0;
        for blue_cap in blue_caps {
            let num: i32 = blue_cap.get(1).unwrap().as_str().parse().unwrap();
            if num > max_blue {
                max_blue = num;
            }
        }
        
        sum += max_red*max_green*max_blue;

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
