# BSD 2-Clause License
#
# Apprise - Push Notification Library.
# Copyright (c) 2025, Chris Caron <lead2gold@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from enum import Enum


class NotifyType(str, Enum):
    """A simple mapping of notification types most commonly used with all types
    of logging and notification services."""

    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    FAILURE = "failure"


# Define our types so we can verify if we need to
NOTIFY_TYPES: frozenset[str] = frozenset(e.value for e in NotifyType)


class NotifyImageSize(str, Enum):
    """A list of pre-defined image sizes to make it easier to work with defined
    plugins."""

    XY_32 = "32x32"
    XY_72 = "72x72"
    XY_128 = "128x128"
    XY_256 = "256x256"


# Define our image sizes so we can verify if we need to
NOTIFY_IMAGE_SIZES: frozenset[str] = \
    frozenset(e.value for e in NotifyImageSize)


class NotifyFormat(str, Enum):
    """A list of pre-defined text message formats that can be passed via the
    apprise library."""

    TEXT = "text"
    HTML = "html"
    MARKDOWN = "markdown"


# Define our formats so we can verify if we need to
NOTIFY_FORMATS: frozenset[str] = frozenset(e.value for e in NotifyFormat)


class OverflowMode(str, Enum):
    """A list of pre-defined modes of how to handle the text when it exceeds
    the defined maximum message size."""

    # Send the data as is; untouched.  Let the upstream server decide how the
    # content is handled.  Some upstream services might gracefully handle this
    # with expected intentions; others might not.
    UPSTREAM = "upstream"

    # Always truncate the text when it exceeds the maximum message size and
    # send it anyway
    TRUNCATE = "truncate"

    # Split the message into multiple smaller messages that fit within the
    # limits of what is expected.  The smaller messages are sent
    SPLIT = "split"


# Define our modes so we can verify if we need to
OVERFLOW_MODES: frozenset[str] = frozenset(e.value for e in OverflowMode)


class ConfigFormat(str, Enum):
    """A list of pre-defined config formats that can be passed via the apprise
    library."""

    # A text based configuration. This consists of a list of URLs delimited by
    # a new line.  pound/hashtag (#) or semi-colon (;) can be used as comment
    # characters.
    TEXT = "text"

    # YAML files allow a more rich of an experience when settig up your
    # apprise configuration files.
    YAML = "yaml"


# Define our configuration formats mostly used for verification
CONFIG_FORMATS: frozenset[str] = frozenset(e.value for e in ConfigFormat)


class ContentIncludeMode(str, Enum):
    """The different Content inclusion modes.

    All content based plugins will have one of these associated with it.
    """

    # - Content inclusion of same type only; hence a file:// can include
    #   a file://
    # - Cross file inclusion is not allowed unless insecure_includes (a flag)
    #   is set to True. In these cases STRICT acts as type ALWAYS
    STRICT = "strict"

    # This content type can never be included
    NEVER = "never"

    # This content can always be included
    ALWAYS = "always"


# Define our file inclusion types so we can verify if we need to
CONTENT_INCLUDE_MODES: frozenset[str] = \
    frozenset(e.value for e in ContentIncludeMode)


class ContentLocation(str, Enum):
    """This is primarily used for handling file attachments.  The idea is to
    track the source of the attachment itself.  We don't want remote calls to a
    server to access local attachments for example.

    By knowing the attachment type and cross-associating it with how we plan on
    accessing the content, we can make a judgement call (for security reasons)
    if we will allow it.

    Obviously local uses of apprise can access both local and remote type
    files.
    """

    # Content is located locally (on the same server as apprise)
    LOCAL = "local"

    # Content is located in a remote location
    HOSTED = "hosted"

    # Content is inaccessible
    INACCESSIBLE = "n/a"


# Define our location types so we can verify if we need to
CONTENT_LOCATIONS: frozenset[str] = frozenset(e.value for e in ContentLocation)


class PersistentStoreMode(str, Enum):
    # Allow persistent storage; write on demand
    AUTO = "auto"

    # Always flush every change to disk after it's saved. This has higher i/o
    # but enforces disk reflects what was set immediately
    FLUSH = "flush"

    # memory based store only
    MEMORY = "memory"


# Define our persistent storage modes so we can verify if we need to
PERSISTENT_STORE_MODES: frozenset[str] = \
    frozenset(e.value for e in PersistentStoreMode)


class PersistentStoreState(str, Enum):
    """Defines the persistent states describing what has been cached."""

    # Persistent Directory is actively cross-referenced against a matching URL
    ACTIVE = "active"

    # Persistent Directory is no longer being used or has no cross-reference
    STALE = "stale"

    # Persistent Directory is not utilizing any disk space at all, however
    # it potentially could if the plugin it successfully cross-references
    # is utilized
    UNUSED = "unused"


# Define our persistent storage states so we can verify if we need to
PERSISTENT_STORE_STATES: frozenset[str] = \
    frozenset(e.value for e in PersistentStoreState)

# This is a reserved tag that is automatically assigned to every
# Notification Plugin
MATCH_ALL_TAG = "all"

# Will cause notification to trigger under any circumstance even if an
# exclusive tagging was provided.
MATCH_ALWAYS_TAG = "always"
