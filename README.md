# Nisi (Backend Django API REST Framework)

## Endpoints

### GET Facebook followings
* Enpoint
fd/fbfollowings/
* input
```
 None
```
* output
```
 DEFAULT
```

### GET Notifications
* Endpoint
  fd/notifications/
* input
  ```
   None
  ```
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

### GET Near users
* Endpoint
  map/nearusers/', map_views.near_users),
* input
  ```
   None
  ```
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

### POST Update location
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
  ```
   DEFAULT
  ```

### POST Follow somebody
* Endpoint
  net/follow
* input
  ```json
  {
    username: "Username of the user who will be followed."
  }
  ```
* output
  ```
   DEFAULT
  ```

### POST Rate somebody
* Endpoint
  net/rate/
* input
  ```json
  {
    rating: rating
  }
  ```
* output
  ```
   DEFAULT
  ```

### GET Somebody's public profile.
* Endpoint
  net/profile/
* input
  ```json
  {
    username: "Username with the requested profile."
  }
  ```
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

### GET My profile
* Endpoint
  nu/profile/
* input
  ```
   None
  ```
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

### POST Sign up
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
  ```
   HTTP 201 if created.
  ```


### POST Sign in
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
  ```
   DEFAULT
  ```

### POST Add social network
* Endpoint
  nu/addsn/
* input
  ```json
  {
    sn:{
      code: SN_CODE,
      username: "Username in the social network."
    }
  }
  ```
* output
  ```
   DEFAULT
  ```

### More

#### DEFAULT
* HTTP200 if okay.
* HTTP40x is client error.
* HTTP50x if server error.

#### NOTIFICATION_TYPE

* 0: Nisi info.
* 1: _username_ is following me.
* 2: _username_ has rated me.
* 3: _username_ has commented a post.

#### SN_CODE
* "tg": "Telegram"
* "tw": "Twitter"
* "ig": "Instagram"
* "fb": "Facebook"

### SN_STATE
* 0: Is not added
* 1: Verified
* 2: In process
* -1: Error
