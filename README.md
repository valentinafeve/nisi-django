# Nisi (Backend Django API REST Framework)

## Endpoints

### Facebook followings
* Enpoint
fd/fbfollowings/
* input
* output
### fd/igfollowings/
* Endpoint
fd/fbfollowings/
* inputs
* output
###
* Endpoint
  fd/notifications/
* input
  None
* output
  ```json
    [
      {
        type: NOTIFICATION_TYPE,
        username: "author of the notification."
        post: "id of post related with the notification."
        content: {
          _comment: "Aditional information about the notification."
        }
      }
    ]
    ```

###
* Endpoint
  map/nearusers/', map_views.near_users),
* input
  None
* output
  ```json
  [
    {
      username: "Username of the user who is near.",
      picture_path: "Profile picture path.",
      rating: rating,
      followed: "true if user is following the user."
    }
  ]
  ```

###
* Endpoint
  map/updatelocation
* input
  ```json
  {
    position: {
      lat: latitude,
      lng: longitude
    }
  }
  ```
* output
  DEFAULT

###
* Endpoint
  net/follow
* input
  {
    username: "Username of the user who will be followed."
  }
* output
  DEFAULT

###
* Endpoint
  net/rate/
* input
  {
    rating: rating
  }
* output
  DEFAULT

###
* Endpoint
  net/profile/
* input
  {
    username: "Username with the requested profile."
  }
* output
  ```json
    {
      rating: rating,
      about: "About, given by the username",
      followers: number_of_followers,
      followings: number_of_follings,
      statistics:{
        antiquity: "Number of years/months/days",
        rated: total_of_rated_people,
        rated_me: total_of_people_who_rated
      },
      sns:{
          fb: "Facebook username.",
          tw: "Twitter username.",
          ig: "Instagram username.",
          tg: "Telegram username."
      },
      posts: [
        {
          post: Post
        }
      ]
    }
  ```

###
* Endpoint
  nu/profile/
* input
  None
* output
  ```json
  {
    username: "username",
    rating: rating,
    about: "About, given by the username",
    followers: number_of_followers,
    followings: number_of_follings,
    sns:{
        fb: {
          username: "Facebook username",
          state: SN_STATE
        },
        tw: {
          username: "Twitter username",
          state: SN_STATE
        },
        ig: {
          username: "Instagram username",
          state: SN_STATE
        },
        tg: {
          username: "Telegram username",
          state: SN_STATE
        },
    },
    statistics:{
      antiquity: "Number of years/months/days",
      rated: total_of_rated_people,
      rated_me: total_of_people_who_rated
    },

  }
  ```

###
* Endpoint
  nu/signup/
* input
  ```json
  {
    username: "username which will be registered.",
    password: "password.",
    phone: "phone number",
    picture: File
  }
  ```
* output
  HTTP201 if created


###
* Endpoint
  nu/signin/
* input
  ```json
  {
    username: "username",
    password: "password"
  }
  ```
* output
  DEFAULT

###
* Endpoint
  nu/settings/
* input
* output

###
* Endpoint
  nu/updatesetting/
* input
* output

###
* Endpoint
  nu/addsn/
* input
* output

### More

#### DEFAULT
>
* HTTP200 if okay.
* HTTP40x is client error.
* HTTP50x if server error.
