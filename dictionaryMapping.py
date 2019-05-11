def mapUserToDict(row):
    result = {}
    result['user_id'] = row[0]
    result['first_name'] = row[1]
    result['last_name'] = row[2]
    result['email'] = row[3]
    result['phone'] = row[4]
    result['username'] = row[5]
    return result

def mapGroupToDict(row):
    result = {}
    result['chat_group_id'] = row[0]
    result['chat_name'] = row[1]
    result['owner_id'] = row[2]
    return result

def mapPostToDict(row):
    result = {}
    result['post_id'] = row[0]
    result['media'] = row[1]
    result['message'] = row[2]
    result['post_date'] = row[3]
    result['chat_group_id'] = row[4]
    result['post_author_id']= row[5]
    return result

def mapPostToDictDETAILED(row, reply):
    result = {}
    result['post_id'] = row[0]
    result['media'] = row[1]
    result['message'] = row[2]
    result['post_date'] = row[3]
    result['chat_group_id'] = row[4]
    result['post_author_id']= row[5]
    result['likes'] = row[6]
    result['dislikes'] = row[7]
    result['username'] = row[8]
    result['first_name'] = row[9]
    result['last_name'] = row[10]
    result['replies'] = reply
    return result

def mapToReactDict(row):
    result = {}
    result['user_id'] = row[0]
    result['first_name'] = row[1]
    result['last_name'] = row[2]
    result['username'] = row[3]
    result['reaction_date'] = row[4]
    return result

def mapReacCountToDict(row):
    result = {}
    result['post_id'] = row[0]
    result['reactions'] = row[1]
    return result

def mapInteractionPerDayToDict(row):
    result = {}
    result['day'] = row[0]
    result['total'] = row[1]
    return result

def mapTrendingTopicToDict(row):
    result = {}
    result['hashtag'] = row[0]
    result['position'] = row[1]
    return result

def mapReplyCountToDict(row):
    result = {}
    result['post_id'] = row[0]
    result['total_replies'] = row[1]
    return result

def mapMostActiveUserToDict(row):
    result = {}
    result['user_id'] = row[0]
    result['interactions'] = row[1]
    return result

def mapReplyToDict(row):
    result = {}
    result['reply_id'] = row[0]
    result['reply_date'] = row[1]
    result['reply_message'] = row[2]
    result['post_id'] = row[3]
    result['username'] = row[4]
    result['first_name'] = row[5]
    result['last_name'] = row[6]
    return result
