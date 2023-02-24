<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;


/**
 * Class __class_name__
 * @version __version__
 * @package App\Console\Commands
 */
class __class_name__ extends Command
{

    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = "__class_name__";


    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = "__summary__";


    /**
     * Create a new command instance.
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
    }


    /**
     * __comment__ __timing__ __remark__
     * @return mixed
     */
    public function handle()
    {

        try {
            // TODO: command function


        } catch (\Exception $ex) {

            // write out a log
            \Log::error($ex->getMessage());

        }

        return;
    }

}

