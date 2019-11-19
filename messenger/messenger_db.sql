--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: chats_attachment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chats_attachment (
    id integer NOT NULL,
    attachment_type character varying(16) NOT NULL,
    url character varying(128) NOT NULL,
    chat_id integer,
    message_id integer
);


--
-- Name: chats_attachment_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.chats_attachment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: chats_attachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.chats_attachment_id_seq OWNED BY public.chats_attachment.id;


--
-- Name: chats_chat; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chats_chat (
    id integer NOT NULL,
    title character varying(128) NOT NULL,
    is_group_chat boolean NOT NULL,
    topic character varying(128) NOT NULL,
    host_id integer,
    last_message_id integer
);


--
-- Name: chats_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.chats_chat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: chats_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.chats_chat_id_seq OWNED BY public.chats_chat.id;


--
-- Name: chats_message; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chats_message (
    id integer NOT NULL,
    content text NOT NULL,
    added_at timestamp with time zone NOT NULL,
    chat_id integer,
    sender_id integer
);


--
-- Name: chats_message_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.chats_message_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: chats_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.chats_message_id_seq OWNED BY public.chats_message.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: user_profile_member; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_profile_member (
    id integer NOT NULL,
    chat_id integer,
    last_read_message_id integer,
    user_id integer
);


--
-- Name: user_profile_member_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_profile_member_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_profile_member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_profile_member_id_seq OWNED BY public.user_profile_member.id;


--
-- Name: user_profile_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_profile_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    avatar character varying(128) NOT NULL
);


--
-- Name: user_profile_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_profile_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: user_profile_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_profile_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_profile_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_profile_user_groups_id_seq OWNED BY public.user_profile_user_groups.id;


--
-- Name: user_profile_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_profile_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_profile_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_profile_user_id_seq OWNED BY public.user_profile_user.id;


--
-- Name: user_profile_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_profile_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: user_profile_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_profile_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_profile_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_profile_user_user_permissions_id_seq OWNED BY public.user_profile_user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: chats_attachment id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_attachment ALTER COLUMN id SET DEFAULT nextval('public.chats_attachment_id_seq'::regclass);


--
-- Name: chats_chat id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_chat ALTER COLUMN id SET DEFAULT nextval('public.chats_chat_id_seq'::regclass);


--
-- Name: chats_message id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_message ALTER COLUMN id SET DEFAULT nextval('public.chats_message_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: user_profile_member id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_member ALTER COLUMN id SET DEFAULT nextval('public.user_profile_member_id_seq'::regclass);


--
-- Name: user_profile_user id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user ALTER COLUMN id SET DEFAULT nextval('public.user_profile_user_id_seq'::regclass);


--
-- Name: user_profile_user_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_groups ALTER COLUMN id SET DEFAULT nextval('public.user_profile_user_groups_id_seq'::regclass);


--
-- Name: user_profile_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_profile_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add Чат	6	add_chat
17	Can change Чат	6	change_chat
18	Can delete Чат	6	delete_chat
19	Can add Сообщение	7	add_message
20	Can change Сообщение	7	change_message
21	Can delete Сообщение	7	delete_message
22	Can add Вложение	8	add_attachment
23	Can change Вложение	8	change_attachment
24	Can delete Вложение	8	delete_attachment
25	Can add Пользователь	9	add_user
26	Can change Пользователь	9	change_user
27	Can delete Пользователь	9	delete_user
28	Can add Участник чата	10	add_member
29	Can change Участник чата	10	change_member
30	Can delete Участник чата	10	delete_member
\.


--
-- Data for Name: chats_attachment; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.chats_attachment (id, attachment_type, url, chat_id, message_id) FROM stdin;
\.


--
-- Data for Name: chats_chat; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.chats_chat (id, title, is_group_chat, topic, host_id, last_message_id) FROM stdin;
1	Test chat #1	f	test	1	7
\.


--
-- Data for Name: chats_message; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.chats_message (id, content, added_at, chat_id, sender_id) FROM stdin;
1	Hello	2019-11-13 19:30:34.023474+03	1	1
2	Hi to you	2019-11-13 19:30:34.023474+03	1	2
3	H	2019-11-13 19:30:34.023474+03	1	1
4	Msg1	2019-11-13 20:09:52.485428+03	1	1
5	Msg2	2019-11-13 20:09:52.485428+03	1	1
6	Msg3	2019-11-13 20:09:52.485428+03	1	1
7	Msg4	2019-11-13 20:09:52.485428+03	1	1
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	chats	chat
7	chats	message
8	chats	attachment
9	user_profile	user
10	user_profile	member
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	chats	0001_initial	2019-10-30 19:13:43.410834+03
2	contenttypes	0001_initial	2019-10-30 19:13:43.532962+03
3	contenttypes	0002_remove_content_type_name	2019-10-30 19:13:43.566124+03
4	auth	0001_initial	2019-10-30 19:13:44.045739+03
5	auth	0002_alter_permission_name_max_length	2019-10-30 19:13:44.078608+03
6	auth	0003_alter_user_email_max_length	2019-10-30 19:13:44.102454+03
7	auth	0004_alter_user_username_opts	2019-10-30 19:13:44.127424+03
8	auth	0005_alter_user_last_login_null	2019-10-30 19:13:44.146158+03
9	auth	0006_require_contenttypes_0002	2019-10-30 19:13:44.156342+03
10	auth	0007_alter_validators_add_error_messages	2019-10-30 19:13:44.179553+03
11	auth	0008_alter_user_username_max_length	2019-10-30 19:13:44.200034+03
12	auth	0009_alter_user_last_name_max_length	2019-10-30 19:13:44.218041+03
13	user_profile	0001_initial	2019-10-30 19:13:44.948061+03
14	admin	0001_initial	2019-10-30 19:13:45.147934+03
15	admin	0002_logentry_remove_auto_add	2019-10-30 19:13:45.187618+03
16	chats	0002_auto_20191030_1613	2019-10-30 19:13:45.404169+03
17	chats	0003_auto_20191030_1613	2019-10-30 19:13:45.444433+03
18	sessions	0001_initial	2019-10-30 19:13:45.626616+03
19	user_profile	0002_auto_20191030_1630	2019-10-30 19:30:10.123114+03
20	chats	0004_auto_20191106_0749	2019-11-06 10:49:30.643029+03
21	chats	0005_auto_20191106_0750	2019-11-06 10:50:20.803926+03
22	chats	0006_auto_20191106_0751	2019-11-06 10:51:31.385224+03
23	chats	0007_auto_20191106_0755	2019-11-06 10:55:03.13448+03
24	chats	0008_auto_20191106_0756	2019-11-06 10:56:31.323532+03
25	chats	0009_auto_20191106_1119	2019-11-06 14:19:43.85832+03
26	user_profile	0003_auto_20191106_1119	2019-11-06 14:19:44.365947+03
27	chats	0010_auto_20191106_1149	2019-11-06 14:49:36.869042+03
28	user_profile	0004_auto_20191106_1149	2019-11-06 14:49:36.931146+03
29	chats	0011_auto_20191106_1447	2019-11-06 17:47:21.773777+03
30	chats	0012_auto_20191113_0954	2019-11-13 12:54:24.989838+03
31	user_profile	0005_auto_20191113_0954	2019-11-13 12:54:25.133068+03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: user_profile_member; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_profile_member (id, chat_id, last_read_message_id, user_id) FROM stdin;
2	1	7	1
1	1	5	2
\.


--
-- Data for Name: user_profile_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_profile_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, avatar) FROM stdin;
1		\N	f	tsar	Vladimir	Putin		f	t	2019-11-13 19:32:09.402445+03	tmp_url
2		\N	f	lil_trump	Donald	Trump		f	t	2019-11-13 19:32:09.463412+03	tmp_url
3		\N	f	winnie_pooh	Xi	Jinping		f	t	2019-11-13 19:32:09.474551+03	tmp_url
\.


--
-- Data for Name: user_profile_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_profile_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: user_profile_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.user_profile_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 30, true);


--
-- Name: chats_attachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.chats_attachment_id_seq', 1, false);


--
-- Name: chats_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.chats_chat_id_seq', 1, true);


--
-- Name: chats_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.chats_message_id_seq', 7, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 31, true);


--
-- Name: user_profile_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_profile_member_id_seq', 2, true);


--
-- Name: user_profile_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_profile_user_groups_id_seq', 1, false);


--
-- Name: user_profile_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_profile_user_id_seq', 3, true);


--
-- Name: user_profile_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_profile_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: chats_attachment chats_attachment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_attachment
    ADD CONSTRAINT chats_attachment_pkey PRIMARY KEY (id);


--
-- Name: chats_chat chats_chat_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_chat
    ADD CONSTRAINT chats_chat_pkey PRIMARY KEY (id);


--
-- Name: chats_message chats_message_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_message
    ADD CONSTRAINT chats_message_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: user_profile_member user_profile_member_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_member
    ADD CONSTRAINT user_profile_member_pkey PRIMARY KEY (id);


--
-- Name: user_profile_user_groups user_profile_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_groups
    ADD CONSTRAINT user_profile_user_groups_pkey PRIMARY KEY (id);


--
-- Name: user_profile_user_groups user_profile_user_groups_user_id_group_id_b5ee7138_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_groups
    ADD CONSTRAINT user_profile_user_groups_user_id_group_id_b5ee7138_uniq UNIQUE (user_id, group_id);


--
-- Name: user_profile_user user_profile_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user
    ADD CONSTRAINT user_profile_user_pkey PRIMARY KEY (id);


--
-- Name: user_profile_user_user_permissions user_profile_user_user_p_user_id_permission_id_34bfca90_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_user_permissions
    ADD CONSTRAINT user_profile_user_user_p_user_id_permission_id_34bfca90_uniq UNIQUE (user_id, permission_id);


--
-- Name: user_profile_user_user_permissions user_profile_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_user_permissions
    ADD CONSTRAINT user_profile_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: user_profile_user user_profile_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user
    ADD CONSTRAINT user_profile_user_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: chats_attachment_chat_id_298338fd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX chats_attachment_chat_id_298338fd ON public.chats_attachment USING btree (chat_id);


--
-- Name: chats_attachment_message_id_5648db92; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX chats_attachment_message_id_5648db92 ON public.chats_attachment USING btree (message_id);


--
-- Name: chats_chat_host_id_8362c0d8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX chats_chat_host_id_8362c0d8 ON public.chats_chat USING btree (host_id);


--
-- Name: chats_chat_last_message_id_9a17bf77; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX chats_chat_last_message_id_9a17bf77 ON public.chats_chat USING btree (last_message_id);


--
-- Name: chats_message_chat_id_f3080004; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX chats_message_chat_id_f3080004 ON public.chats_message USING btree (chat_id);


--
-- Name: chats_message_sender_id_4f3659eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX chats_message_sender_id_4f3659eb ON public.chats_message USING btree (sender_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: user_profile_member_chat_id_c61fb0df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_member_chat_id_c61fb0df ON public.user_profile_member USING btree (chat_id);


--
-- Name: user_profile_member_last_read_message_id_84da936c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_member_last_read_message_id_84da936c ON public.user_profile_member USING btree (last_read_message_id);


--
-- Name: user_profile_member_user_id_90581ba0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_member_user_id_90581ba0 ON public.user_profile_member USING btree (user_id);


--
-- Name: user_profile_user_groups_group_id_7cd4b3f5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_user_groups_group_id_7cd4b3f5 ON public.user_profile_user_groups USING btree (group_id);


--
-- Name: user_profile_user_groups_user_id_cefab937; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_user_groups_user_id_cefab937 ON public.user_profile_user_groups USING btree (user_id);


--
-- Name: user_profile_user_user_permissions_permission_id_fcfd8bc0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_user_user_permissions_permission_id_fcfd8bc0 ON public.user_profile_user_user_permissions USING btree (permission_id);


--
-- Name: user_profile_user_user_permissions_user_id_bdd85bfb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_user_user_permissions_user_id_bdd85bfb ON public.user_profile_user_user_permissions USING btree (user_id);


--
-- Name: user_profile_user_username_35ac9403_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX user_profile_user_username_35ac9403_like ON public.user_profile_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chats_attachment chats_attachment_chat_id_298338fd_fk_chats_chat_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_attachment
    ADD CONSTRAINT chats_attachment_chat_id_298338fd_fk_chats_chat_id FOREIGN KEY (chat_id) REFERENCES public.chats_chat(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chats_attachment chats_attachment_message_id_5648db92_fk_chats_message_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_attachment
    ADD CONSTRAINT chats_attachment_message_id_5648db92_fk_chats_message_id FOREIGN KEY (message_id) REFERENCES public.chats_message(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chats_chat chats_chat_host_id_8362c0d8_fk_user_profile_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_chat
    ADD CONSTRAINT chats_chat_host_id_8362c0d8_fk_user_profile_user_id FOREIGN KEY (host_id) REFERENCES public.user_profile_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chats_chat chats_chat_last_message_id_9a17bf77_fk_chats_message_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_chat
    ADD CONSTRAINT chats_chat_last_message_id_9a17bf77_fk_chats_message_id FOREIGN KEY (last_message_id) REFERENCES public.chats_message(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chats_message chats_message_chat_id_f3080004_fk_chats_chat_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_message
    ADD CONSTRAINT chats_message_chat_id_f3080004_fk_chats_chat_id FOREIGN KEY (chat_id) REFERENCES public.chats_chat(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chats_message chats_message_sender_id_4f3659eb_fk_user_profile_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chats_message
    ADD CONSTRAINT chats_message_sender_id_4f3659eb_fk_user_profile_user_id FOREIGN KEY (sender_id) REFERENCES public.user_profile_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_user_profile_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_profile_user_id FOREIGN KEY (user_id) REFERENCES public.user_profile_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_member user_profile_member_chat_id_c61fb0df_fk_chats_chat_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_member
    ADD CONSTRAINT user_profile_member_chat_id_c61fb0df_fk_chats_chat_id FOREIGN KEY (chat_id) REFERENCES public.chats_chat(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_member user_profile_member_last_read_message_id_84da936c_fk_chats_mes; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_member
    ADD CONSTRAINT user_profile_member_last_read_message_id_84da936c_fk_chats_mes FOREIGN KEY (last_read_message_id) REFERENCES public.chats_message(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_member user_profile_member_user_id_90581ba0_fk_user_profile_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_member
    ADD CONSTRAINT user_profile_member_user_id_90581ba0_fk_user_profile_user_id FOREIGN KEY (user_id) REFERENCES public.user_profile_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_user_groups user_profile_user_gr_user_id_cefab937_fk_user_prof; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_groups
    ADD CONSTRAINT user_profile_user_gr_user_id_cefab937_fk_user_prof FOREIGN KEY (user_id) REFERENCES public.user_profile_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_user_groups user_profile_user_groups_group_id_7cd4b3f5_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_groups
    ADD CONSTRAINT user_profile_user_groups_group_id_7cd4b3f5_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_user_user_permissions user_profile_user_us_permission_id_fcfd8bc0_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_user_permissions
    ADD CONSTRAINT user_profile_user_us_permission_id_fcfd8bc0_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_profile_user_user_permissions user_profile_user_us_user_id_bdd85bfb_fk_user_prof; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profile_user_user_permissions
    ADD CONSTRAINT user_profile_user_us_user_id_bdd85bfb_fk_user_prof FOREIGN KEY (user_id) REFERENCES public.user_profile_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

