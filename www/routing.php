<?php
/**
 * Redirect from a form GET on the home page to a more human readable/bookmarkable/pastable URL format
 *
 * Choosing 302 redirect specifically as the redirection strategy may change and cached destination would be bad.
 *
 */

$baseUrl = 'http://first-contact.org';
$locationPage = 'show';

if (isset($_REQUEST['lang']) && isset($_REQUEST['loc'])) {
    $redirectURL = $baseUrl . '/' . $locationPage . '/' . safeString($_REQUEST['lang']) . '/' . safeString($_REQUEST['loc']);
    header('Location: ' . $redirectURL, true, 302);
}

/**
 * Return string safe in this context - alpha only
 * @param $string
 * @return $string
 *
 */
function safeString($string) {
    return preg_replace("/[^A-Za-z]/", '', $string);
}
?>
