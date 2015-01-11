<?php

$inputs = [
    "wtf that was unfair",
    "gl all hf",
    "imo that was wp. Anyway I've g2g"
];

$outputs = [
    "what the fuck that was unfair",
    "good luck all have fun",
    "in my opinion that was well played. Anyway I've got to go"
];

function expandAbbreviation($string) {
    $wordlist = [
        "/lol/" => "laugh out loud",
        "/dw/"  => "don't worry",
        "/hf/"  => "have fun",
        "/gg/"  => "good game",
        "/brb/" => "be right back",
        "/g2g/" => "got to go",
        "/wtf/" => "what the fuck",
        "/wp/"  => "well played",
        "/gl/"  => "good luck",
        "/imo/" => "in my opinion"
    ];

    return preg_replace(array_keys($wordlist), array_values($wordlist), $string);
}

foreach($inputs as $input) {
    echo expandAbbreviation($input) . '<br />';
}
