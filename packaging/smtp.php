<?php

///////////////////////////////////////////////////////////////////////////////
// B O O T S T R A P
///////////////////////////////////////////////////////////////////////////////

$bootstrap = getenv('CLEAROS_BOOTSTRAP') ? getenv('CLEAROS_BOOTSTRAP') : '/usr/clearos/framework/shared';
require_once $bootstrap . '/bootstrap.php';

///////////////////////////////////////////////////////////////////////////////
// T R A N S L A T I O N S
///////////////////////////////////////////////////////////////////////////////

clearos_load_language('smtp_plugin');

///////////////////////////////////////////////////////////////////////////////
// C O N F I G
///////////////////////////////////////////////////////////////////////////////

$plugin['name'] = lang('smtp_plugin_smtp_server_user');
$plugin['description'] = lang('smtp_plugin_app_description');
$plugin['enabled'] = TRUE;
