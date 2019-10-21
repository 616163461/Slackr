import React from 'react';
import * as routecall from '../../utils/routecall';

import {
  Badge,
  IconButton,
} from '@material-ui/core';

import ThumbUpIcon from '@material-ui/icons/ThumbUp';
import ThumbUpOutlinedIcon from '@material-ui/icons/ThumbUpOutlined';

import { url } from '../../utils/constants';

import AuthContext from '../../AuthContext';

function MessageReact({
  message_id,
  reacts = [] /* [{ react_id, u_ids }] */,
}) {

  const token = React.useContext(AuthContext);

  const messageReact = (is_reacted) => {
    if (is_reacted) {
      routecall.post(`${url}/message/unreact`, {
        token,
        message_id,
        react_id: 1 /* FIXME */,
      });
    } else {
      routecall.post(`${url}/message/react`, {
        token,
        message_id,
        react_id: 1 /* FIXME */,
      });
    }
  };

  let thumbUpCount = 0;
  let is_reacted = false;
  const thumbUpIndex = reacts.findIndex((react) => react.react_id === 1);
  if (thumbUpIndex !== -1) {
    thumbUpCount = reacts[thumbUpIndex].u_ids.length;
    is_reacted = reacts[thumbUpIndex].is_this_user_reacted;
  }

  return (
    <Badge
      anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      badgeContent={thumbUpCount}
      color="secondary"
    >
      <IconButton
        onClick={() => messageReact(is_reacted)}
        style={{ margin: 1 }}
        size="small"
        edge="end"
        aria-label="delete"
      >
        {is_reacted ? (
          <ThumbUpIcon fontSize="small" />
          ) : (
          <ThumbUpOutlinedIcon fontSize="small" />
        )}
      </IconButton>
    </Badge>
  );
}

export default MessageReact;
