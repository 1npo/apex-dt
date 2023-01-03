BEGIN TRANSACTION;

--  ____ ___  _    ___ ____ ___  _    ____ ____
--  |__| |__] |     |  |__| |__] |    |___ [__
--  |  | |    |     |  |  | |__] |___ |___ ___]
--
--  Tables that contain data retrieved from the Apex Legends Status (ALS) API
--

CREATE TABLE IF NOT EXISTS api_apex_news (
	news_id			INTEGER NOT NULL,
	date_updated	INTEGER NOT NULL,
	news_title		TEXT NOT NULL,
	news_desc		TEXT NOT NULL,
	news_link		TEXT NOT NULL,
	PRIMARY KEY(news_id),
	CONSTRAINT unique_news_item UNIQUE(news_title, news_desc, news_link)
);

CREATE TABLE IF NOT EXISTS api_server_status (
	server_id			INTEGER NOT NULL,
	date_updated		INTEGER NOT NULL,
	platform_name		TEXT NOT NULL,
	server_name			TEXT NOT NULL,
	time_checked		INTEGER,
	response_code		INTEGER,
	response_time		INTEGER,
	server_status		TEXT,
	PRIMARY KEY(status_id),
	CONSTRAINT unique_server_status_snapshot UNIQUE(
		platform_name,
		server_name,
		time_checked,
		response_code,
		response_time,
		server_status)
);

CREATE TABLE IF NOT EXISTS api_map_rotations (
	map_rotation_id					INTEGER NOT NULL,
	date_updated					INTEGER NOT NULL,
	game_mode						TEXT NOT NULL,
	current_map						TEXT NOT NULL,
	current_map_duration_min		INTEGER NOT NULL,
	current_map_duration_sec		INTEGER NOT NULL,
	current_map_start_time			INTEGER NOT NULL,
	current_map_end_time			INTEGER NOT NULL,
	current_map_remaining_sec		INTEGER NOT NULL,
	current_map_remaining_min		INTEGER NOT NULL,
	current_map_remaining_timer		TEXT NOT NULL,
	next_map						TEXT NOT NULL,
	next_map_duration_min			INTEGER NOT NULL,
	next_map_duration_sec			INTEGER NOT NULL,
	next_map_start_time				INTEGER NOT NULL,
	next_map_end_time				INTEGER NOT NULL,
	PRIMARY KEY(map_rotation_id),
	CONSTRAINT unique_map_rotation UNIQUE(
		current_map_start_time,
		current_map_end_time,
		next_map_start_time,
		next_map_end_time)
);

CREATE TABLE IF NOT EXISTS api_crafting_rotations (
	crafting_rotation_id			INTEGER NOT NULL,
	date_updated					INTEGER NOT NULL,
	crafting_rotation_name			TEXT NOT NULL,
	crafting_rotation_type			TEXT NOT NULL,
	crafting_rotation_start_date	INTEGER NOT NULL,
	crafting_rotation_end_date		INTEGER NOT NULL,
	PRIMARY KEY(crafting_rotation_id),
	CONSTRAINT unique_crafting_rotation UNIQUE(
		crafting_rotation_start_date,
		crafting_rotation_end_date)
);

CREATE TABLE IF NOT EXISTS api_crafting_bundle_items (
	bundle_item_id			INTEGER NOT NULL,
	date_updated			INTEGER NOT NULL,
	rotation_id				INTEGER NOT NULL,
	bundle_item_name		TEXT NOT NULL,
	bundle_item_cost		INTEGER NOT NULL,
	bundle_item_rarity		TEXT NOT NULL,
	PRIMARY KEY(bundle_item_id),
	FOREIGN KEY(rotation_id) REFERENCES crafting_rotations(rotation_id),
	CONSTRAINT unique_crafting_bundle UNIQUE(
		bundle_item_id,
		bundle_item_name,
		bundle_item_cost,
		bundle_item_rarity)
);

CREATE TABLE IF NOT EXISTS api_legends (
	legend_id				INTEGER NOT NULL,
	date_updated			INTEGER NOT NULL,
	legend_name				TEXT NOT NULL,
	legend_frame			TEXT NOT NULL,
	legend_frame_rarity		TEXT NOT NULL,
	legend_intro			TEXT NOT NULL,
	legend_intro_rarity		TEXT NOT NULL,
	legend_pose				TEXT NOT NULL,
	legend_pose_rarity		TEXT NOT NULL,
	legend_skin				TEXT NOT NULL,
	legend_skin_rarity		TEXT NOT NULL,
	PRIMARY KEY(legend_id),
	CONSTRAINT unique_legend UNIQUE(
		legend_name,
		legend_frame,
		legend_frame_rarity,
		legend_intro,
		legend_intro_rarity,
		legend_pose,
		legend_pose_rarity,
		legend_skin,
		legend_skin_rarity)
);

CREATE TABLE IF NOT EXISTS api_legend_trackers (
	tracker_id						INTEGER NOT NULL,
	date_updated					INTEGER NOT NULL,
	legend_id						INTEGER NOT NULL,
	tracker_name					TEXT NOT NULL,
	tracker_value					INTEGER NOT NULL,
	tracker_rank_pos				INTEGER NOT NULL,
	tracker_rank_percent			REAL NOT NULL,
	tracker_rank_pos_platspec		INTEGER NOT NULL,
	tracker_rank_percent_platspec	REAL NOT NULL,
	PRIMARY KEY(tracker_id),
	FOREIGN KEY(legend_id) REFERENCES legends(legend_id),
	CONSTRAINT unique_tracker UNIQUE(
		legend_id,
		tracker_name,
		tracker_value,
		tracker_rank_pos,
		tracker_rank_percent,
		tracker_rank_pos_platspec,
		tracker_rank_percent_platspec)
);

CREATE TABLE IF NOT EXISTS api_legend_badges (
	badge_id			INTEGER NOT NULL,
	date_updated		INTEGER NOT NULL,
	legend_id			INTEGER NOT NULL,
	badge_name			TEXT NOT NULL,
	badge_category		TEXT NOT NULL,
	badge_value			INTEGER NOT NULL,
	PRIMARY KEY(badge_id),
	FOREIGN KEY(legend_id) REFERENCES legends(legend_id),
	CONSTRAINT unique_badge UNIQUE(legend_id, badge_name, badge_category)
);

CREATE TABLE IF NOT EXISTS api_players (
	player_id			INTEGER NOT NULL,
	date_updated		INTEGER NOT NULL,
	uid					INTEGER NOT NULL,
	pid					INTEGER NOT NULL,
	platform			TEXT NOT NULL,
	current_state		TEXT NOT NULL,
	is_in_game			INTEGER NOT NULL,		-- boolean
	is_online			INTEGER NOT NULL,		-- boolean
	current_legend		TEXT NOT NULL,
	ban_is_active		INTEGER NOT NULL,		-- boolean
	ban_last_reason		TEXT NOT NULL,
	ban_remaining_sec	INTEGER NOT NULL,
	name_in_game		TEXT NOT NULL,
	name_on_platform	TEXT NOT NULL,
	PRIMARY KEY(player_id),
	CONSTRAINT unique_player UNIQUE(
		uid,
		pid,
		platform,
		current_state,
		is_in_game,
		is_online,
		current_legend,
		ban_is_active,
		ban_last_reason,
		ban_remaining_sec,
		name_in_game,
		name_on_platform)
);

CREATE TABLE IF NOT EXISTS api_player_stats (
	stat_id						INTEGER NOT NULL,
	date_updated				INTEGER NOT NULL,
	player_id					INTEGER NOT NULL,
	arenas_damage				INTEGER NOT NULL,
	arenas_kills				INTEGER NOT NULL,
	arenas_wins					INTEGER NOT NULL,
	jacksons_bow_out_dmg		INTEGER NOT NULL,
	scout_of_action_targets		INTEGER NOT NULL,
	smoke_show_dmg				INTEGER NOT NULL,
	br_damage					INTEGER NOT NULL,
	br_kills					INTEGER NOT NULL,
	br_wins						INTEGER NOT NULL,
	PRIMARY KEY(stat_id),
	FOREIGN KEY(player_id) REFERENCES players(player_id),
	CONSTRAINT stats_updated UNIQUE(
		player_id,
		arenas_damage,
		arenas_kills,
		arenas_wins,
		jacksons_bow_out_dmg,
		scout_of_action_targets,
		smoke_show_dmg,
		br_damage,
		br_kills,
		br_wins)
);

CREATE TABLE IF NOT EXISTS api_player_rank_levels (
	rank_id					INTEGER NOT NULL,
	date_updated			INTEGER NOT NULL,
	player_id				INTEGER NOT NULL,
	account_level			INTEGER NOT NULL,
	account_prestige		INTEGER NOT NULL,
	percent_to_next_level	REAL NOT NULL,
	br_rank					TEXT NOT NULL,
	br_rank_div				INTEGER NOT NULL,
	br_rank_score			INTEGER NOT NULL,
	br_rank_season			TEXT NOT NULL,
	arenas_rank				TEXT NOT NULL,
	arenas_rank_div			INTEGER NOT NULL,
	arenas_rank_score		INTEGER NOT NULL,
	arenas_rank_season		TEXT NOT NULL,
	PRIMARY KEY(rank_id),
	FOREIGN KEY(player_id) REFERENCES players(player_id),
	CONSTRAINT ranks_updated UNIQUE(
		player_id,
		level,
		prestige,
		percent_to_next_level,
		br_rank,
		br_rank_div,
		br_rank_score,
		br_rank_season,
		arenas_rank,
		arenas_rank_div,
		arenas_rank_score,
		arenas_rank_season)
);

CREATE TABLE IF NOT EXISTS api_player_match_histories (
	match_id			INTEGER NOT NULL,
	date_updated		INTEGER NOT NULL,
	player_id			INTEGER NOT NULL,
	match_start_time	INTEGER NOT NULL,
	match_end_time		INTEGER NOT NULL,
	match_length_sec	INTEGER NOT NULL,
	match_game_mode		TEXT NOT NULL,
	match_map			TEXT NOT NULL,
	match_kills			INTEGER NOT NULL,
	match_damage		INTEGER NOT NULL,
	match_win			INTEGER NOT NULL,		-- boolean
	score_after			INTEGER NOT NULL,
	score_change		INTEGER NOT NULL,
	is_party_full		INTEGER NOT NULL,		-- boolean
	legend_played		TEXT NOT NULL,
	PRIMARY KEY(match_id),
	FOREIGN KEY(player_id) REFERENCES players(player_id),
	CONSTRAINT unique_match UNIQUE(match_start_time, match_end_time)
);


--  _ _ _ _ _  _ _    ___ ____ ___  _    ____ ____
--  | | | | |_/  |     |  |__| |__] |    |___ [__
--  |_|_| | | \_ |     |  |  | |__] |___ |___ ___]
--
--  Tables that contain data scraped from the Apex Legends Fandom Wiki page
--

-- TODO: Add these tables


COMMIT;

