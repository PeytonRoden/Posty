-- Create User table
CREATE TABLE User (
    user_id SERIAL       NOT NULL,
    first_name    VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    univserity VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

-- Create Comment table
CREATE TABLE Comment (

    comment_id SERIAL       NOT NULL,
    user_id    INT          NOT NULL,
    post_id    INT          NOT NULL,
    comment_text VARCHAR(255) NOT NULL,
    comment_datetime DATETIME NOT NULL,
    parent_comment_id INT     NULL,
    PRIMARY KEY (comment_id),

    FOREIGN KEY (user_id)
        REFERENCES User(user_id),

    FOREIGN KEY (post_id)
        REFERENCES Post(post_id)
);


-- Create Post table
CREATE TABLE Post (
    post_id SERIAL       NOT NULL,
    user_id    INT          NOT NULL,
    post_title VARCHAR(255) NOT NULL,
    post_title VARCHAR(255) NOT NULL,
    post_datetime DATETIME NOT NULL,
    univserity VARCHAR(255) NOT NULL,

    number_likes   INT          NOT NULL,
    number_reposts   INT          NOT NULL,
    number_comments   INT          NOT NULL,

    PRIMARY KEY (post_id),

    FOREIGN KEY (user_id)
        REFERENCES Post(user_id)
);


-- Create Like table
CREATE TABLE LIKE_ (
    
    like_id SERIAL       NOT NULL,
    user_id    INT          NOT NULL,
    post_id    INT          NOT NULL,
    PRIMARY KEY (like_id),

    FOREIGN KEY (user_id)
        REFERENCES User(user_id),

    FOREIGN KEY (post_id)
        REFERENCES Post(post_id)
);


-- Create Repost table
CREATE TABLE Repost (
    
    repost_id SERIAL       NOT NULL,
    reposter_user_id    INT          NOT NULL,
    poster_user_id    INT          NOT NULL,
    post_id    INT          NOT NULL,
    PRIMARY KEY (like_id),

    FOREIGN KEY (reposter_user_id)
        REFERENCES User(user_id),

    FOREIGN KEY (post_id)
        REFERENCES Post(post_id),

    FOREIGN KEY (poster_user_id)
        REFERENCES User(user_id),

);