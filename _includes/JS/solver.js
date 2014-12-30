/**
* Reverse string
*
*  Args:
*   to_reverse: String to be reversed.
*
*  Returns:
*   Reversed string, in the format of a json object.
*/
function solve_reverse_string(to_reverse) {
  return str.split('').reverse().join('');
}

/**
* Find index of needle in Haystack array.
*
*  Args:
*   needle: String to be found.
*   haystack: Array with values to be searched.
*
*  Returns:
*   Index of the position of the needle.
*/
function solve_haystack(needle, haystack) {
  return haystack.indexOf(needle);
}

/**
* Find all the words in list that don't start with given prefix.
*
*  Args:
*   prefix: Prefix to be found.
*   strings: Array with values to be searched.
*
*  Returns:
*   List filtered with only values that `don't` start with prefix.
*/
function solve_prefix(prefix, strings) {
    return strings.filter(
        function(element) {
            if(element.substring(0, prefix.length) != prefix)
                return element;
        });
}

/**
* Return date increased with interval in the ISO 8601 format.
*
*  Args:
*   needle: Interval to be added to time.
*   datestamp: Initial date.
*
*  Returns:
*   The new data in the ISO 8601 format.
*/
function solve_dating(interval, datestamp) {
  var newDate = new Date(datestamp);
  newDate
    .setSeconds(newDate.getSeconds() + interval);
  return newDate.toISOString();
}
