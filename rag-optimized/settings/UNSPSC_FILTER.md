# UNSPSC_FILTER - iPurchase System Setting

**Category:** Uncategorized

To modify this setting to control which UNSPSC codes are available to choose from. The syntax for this settings uses the CAN-DO functionality similar to a lot of the other settings. To re-cap, the CAN-DO functionality uses a comma-separated list of values that are either "good" or "bad". Any value that begins with an exclamation point, is "bad" and won't be shown. You can use wildcards to match whole ranges of codes. Here are some examples; It's currently set to !*0000,*00,!* This means anything that ends with 4 zeros is "bad" and won't be shown. Anything that ends with 2 zeros is "good" and will be shown. All others are bad. The CAN-DO reads from left to right until it is able to match your code with one of the entries in the value. Let's say the code is 24102010. It first checks that number against !*0000. Since it does not match it moves on to the next entry, *00. Since it also does not match that one, it moves on to the last entry !*. This time code 24102010 does match * and since there is an exclamation point in front of it, it marks it as "bad" and does not display. The first !*0000 will eliminated the codes similar to 24000000 and 241000000 � they both end in 4 zeros. So, the Segment and Family codes will not be displayed. The *00 will show all remaining which end with 2 zeros. Since we already eliminated the Segment and Family coeds with the first entry, only the Class codes will display. The final !* will eliminate anything else, basically anything that doesn't end with 00 will get eliminated. If you want to remove the "Live Animal Segment" altogether, and it is segment 10000000. To do this change the current value of the UNSPSC_FILTER as follows: !10*,!*0000,*00,!* You will notice I added !10* to the beginning of the list. If you also want to remove segment 11000000, you should do the same. !10*,!11*,!*0000,*00,!* You will notice I added !11* after the !10*. If you want to keep the Classes that are in Family with 1120. To do this we are going to move some things around because the left-to-right order is important. Remember the CAN-DO will keep reading until it finds a match. !10*,!*0000,1120*00,!11*,*00,!* !10* - First we will eliminate anything that starts with a 10 because we don't care at all about "Live Animals" !*0000 - Next we will eliminate all that end with 4 or 6 zeros � Segment and Family 1120*00 � Next we will keep all classes that start with 1120 and end with 00. If it were just 1120* and didn't have the "00" at the end, then all codes including Component level would also be valid. We do not want that. By adding "00" at the end, we are telling the system that not only does it need to begin with 1120, but we only want the classes that begin with 1120. !11* - Next, eliminate anything else that begins with 11. *00 � Everything else that ends with 00 is good. !* - All others bad

### How It Works

This setting uses [Can-Do list format](../../reference/can-do-list-format.md) for specifying users and groups.

### Valid Values

| Value | Behavior |
|-------|----------|
| `*` (asterisk) | Everyone/all users |
| Blank/empty | No one/disabled |
| User/Group list | Only specified users/groups |

### Setting Details

| Property | Value |
|----------|-------|
| **Setting Name** | UNSPSC_FILTER |
| **Category** | Uncategorized |
| **Owner** | Purchasing |
| **Default Value** | * |

### How to Query

```sql
SELECT pf_chr1 FROM PUB.pf_mstr
WHERE pf_us_id = 'SYSTEM' AND pf_group = 'DEFAULT' AND pf_attr = 'UNSPSC_FILTER'
```
