from dataclasses import dataclass
from datetime import datetime

from apex_dt.domain.base import Entity, ValueObject


@dataclass(frozen=True)
class NewsItem(ValueObject):
    """A value object that represents an EA/Apex News bulletin item"""
    news_id: int = None
    news_title: str = None
    news_desc: str = None
    news_link: str = None


@dataclass
class ApexServer(Entity):
    """An entity that represents an Apex Legends server"""
    server_id: int = None
    platform_name: str = None
    server_name: str = None
    server_status: str = None
    response_code: int = Non
    response_time: int = None
    time_checked: datetime = None


@dataclass(frozen=True)
class MapRotation(ValueObject):
    """A value object that represents a map rotation"""
    map_rotation_id: int = None
    game_mode: str = None
    current_map: str = None
    current_map_duration_min: int = None
    current_map_duration_sec: int = None
    current_map_start_time: datetime = None
    current_map_end_time: datetime = None
    current_map_remaining_sec: int = None
    current_map_remaining_min: int = None
    current_map_remaining_timer: str = None
    next_map: str = None
    next_map_duration_min: int = None
    next_map_duration_sec: int = None
    next_map_start_time: datetime = None
    next_map_end_time: datetime = None


@dataclass(frozen=True)
class CraftingRotation(ValueObject):
    """A value object that represents a crafting rotation"""
    crafting_rotation_id: int = None
    crafting_rotation_name: str = None
    crafting_rotation_type: str = None
    crafting_rotation_start_date: datetime = None
    crafting_rotation_end_date: datetime = None
    crafting_rotation_contents: list[CraftingBundleItem] = None


@dataclass(frozen=True)
class CraftingBundleItem(ValueObject):
    """A value object that represents an item in a crafting rotation"""
    bundle_item_id: int = None
    bundle_item_name: str = None
    bundle_item_cost: int = None
    bundle_item_rarity: str = None


@dataclass
class LegendTracker(Entity):
    """An entity that represents a Legend's stats tracker"""
    tracker_id: int = None
    tracker_name: str = None
    tracker_value: int = None
    tracker_rank_pos: int = None
    tracker_rank_pos_platspec: int = None
    tracker_rank_percent: float = None
    tracker_rank_percent_platspec: float = None


@dataclass
class LegendBadge(Entity):
    """An entity that represents a Legend's badge"""
    badge_id: int = None
    badge_name: str = None
    badge_category: str = None
    bdage_value: int = None


@dataclass
class ApexLegend(Entity):
    """An entity that represents an Apex Legend"""
    legend_id: int = None
    legend_name: str = None
    legend_frame: str = None
    legend_intro: str = None
    legend_pose: str = None
    legend_skin: str = None
    legend_frame_rarity: str = None
    legend_intro_rarity: str = None
    legend_pose_rarity: str = None
    legend_skin_rarity: str = None
    legend_badges: list[LegendBadge] = None
    legend_trackers: list[LegendTracker] = None


@dataclass
class PlayerStats(Entity):
    """An entity that represents a player's stats"""
    stat_id: int = None
    arenas_damage: int = None
    arenas_kills: int = None
    arenas_wins: int = None
    br_damage: int = None
    br_kills: int = None
    br_wins: int = None
    smoke_show_dmg: int = None
    scout_of_actions_targets: int = None
    jacksons_bow_out_dmg: int = None
 

@dataclass
class PlayerRanks(Entity):
    """An entity that represents a player's current rank"""
    rank_id: int = None
    account_level: int = None
    account_prestive: int = None
    percent_to_next_level: float = None
    arenas_rank: str = None
    arenas_rank_div: int = None
    arenas_rank_score: int = None
    arenas_rank_season: str = None
    br_rank: str = None
    br_rank_div: int = None
    br_rank_score: int = None
    br_rank_season: str = None


@dataclass
class ApexLegendsPlayer(Entity):
    """An entity that represents an Apex Legends player"""
    player_id: int = None
    uid: int = None
    pid: int = None
    platform: str = None
    name_in_game: str = None
    name_on_platform: str = None
    current_state: str = None
    current_legend: str = None
    is_online: bool = None
    is_in_game: bool = None
    ban_is_active: bool = None
    ban_last_reason: str = None
    ban_remaining_sec: int = None
    player_stats: PlayerStats = PlayerStats()
    player_ranks: PlayerRanks = PlayerRanks()
    

@dataclass(frozen=True)
class Match(ValueObject):
    """A value object that represents the results of a match"""
    match_id: int = None
    match_start_time: datetime = None
    match_end_time: datetime = None
    match_length_sec: int = None
    match_game_mode: str = None
    match_map: str = None
    match_kills: int = None
    match_damage: int = None
    match_win: bool = None
    score_after: int = None
    score_change: int = None
    is_party_full: bool = None
    legend_played: str = None

